from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customer_set',
        blank=True,
        help_text='The groups this user belongs to',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customer_set',
        blank=True,
        help_text='SPecific permissions for this user',
        verbose_name='user permissions'
    )

