from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    profile_photo = models.ImageField(upload_to='images/profile_photos/', blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')


