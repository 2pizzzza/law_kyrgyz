from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class User(AbstractUser):

    gender = models.TextField()
    citizenship = models.TextField()
    date_of_birth = models.TextField()
    document_id = models.TextField()
    date_of_expiry = models.TextField()
    place_of_birth = models.TextField()
    authority = models.TextField()
    date_of_issue = models.TextField()
    ethnicity = models.TextField()
    personal_number = models.TextField()

    username = None
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    middle_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_users',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_users',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.email
