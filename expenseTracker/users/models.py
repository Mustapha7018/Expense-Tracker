from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(blank=True, null=True, upload_to='profiles/')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.first_name)

