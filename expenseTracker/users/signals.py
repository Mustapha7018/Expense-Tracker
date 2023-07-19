from django.db import transaction
from django.contrib.auth.models import User
from .models import Profile, UserActivity
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from datetime import datetime

@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance,
            full_name=instance.get_full_name()
        )
    else:
        profile, created = Profile.objects.get_or_create(user=instance)
        if not created:
            profile.full_name = instance.get_full_name()
            profile.save()
            
    UserActivity.objects.create(
        user=instance, 
        operation_type='Add User' if created else 'Update User', 
        entity_type='Admin' if instance.is_staff else 'User',
        time=datetime.now()
    )


@receiver(pre_delete, sender=User)
def delete_profile(sender, instance, **kwargs):
    UserActivity.objects.create(
        user=instance,
        operation_type='Delete User',
        entity_type='Admin' if instance.is_staff else 'User',
        time=datetime.now()
    )

