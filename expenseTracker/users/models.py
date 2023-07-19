from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('staff', 'Staff'),
    )

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(blank=True, null=True, upload_to='profiles/',default="profiles/user-default.svg")
    created = models.DateTimeField(auto_now_add=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='staff', blank=True, null=True)




    def __str__(self):
        return str(self.user.first_name)



class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    operation_type = models.CharField(
        max_length=50,
        choices=[
            ('Add User', 'Added User'),
            ('Update User', 'Updated User'),
            ('Delete User', 'Deleted User'),
            ('Add Income', 'Added Income'),
            ('Update Income', 'Updated Income'),
            ('Delete Income', 'Deleted Income'),
            ('Add Expense', 'Added Expense'),
            ('Update Expense', 'Updated Expense'),
            ('Delete Expense', 'Deleted Expense'),
            ('Add Wallet', 'Added Wallet'),
            ('Update Wallet', 'Updated Wallet'),
            ('Delete Wallet', 'Deleted Wallet'),
        ]
    )
    operation_desc = models.CharField(max_length=255)
    entity_type = models.CharField(max_length=50, null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.operation_type}'
