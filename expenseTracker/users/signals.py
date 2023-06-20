from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance
            # username=instance.username,
            #email=instance.email,
            #name=instance.get_full_name()
        )

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

"""@receiver(post_save, sender=Profile)
def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name,
        user.username = profile.username,
        user.email = profile.email,
        user.save()


@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    profile = instance
    user = profile.user

    if user is not None:
        user.delete()"""

    