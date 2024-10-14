from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    # اگر نیاز به فیلدهای اضافی داری، می‌تونی اینجا اضافه کنی.
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # تغییر نام معکوس برای جلوگیری از تداخل
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # تغییر نام معکوس برای جلوگیری از تداخل
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
