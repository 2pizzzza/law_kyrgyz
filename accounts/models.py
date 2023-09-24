from django.contrib.auth.models import AbstractUser
from django.db import models


class Notification(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_date"]


class User(AbstractUser):

    gender = models.CharField(max_length=50)
    citizenship = models.CharField(max_length=50)
    date_of_birth = models.CharField(max_length=50)
    document_id = models.CharField(max_length=50)
    date_of_expiry = models.CharField(max_length=50)
    place_of_birth = models.CharField(max_length=50)
    authority = models.CharField(max_length=50)
    date_of_issue = models.CharField(max_length=50)
    ethnicity = models.CharField(max_length=50)
    personal_number = models.CharField(max_length=50)

    username = None
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    middle_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE, null=True)

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
        return self.first_name + " " + self.last_name
