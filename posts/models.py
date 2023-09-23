from accounts.models import User
from django.db import models

CATEGORIES = (("Образование", "Образование"),
              ("Медицина", "Медицина"),
              ("Природа", "Природа"),
              ("Судебная", "Судебная"),
              ("Бизнес", "Бизнес"),
              ("СМИ", "СМИ"),
              )

class Post(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=100, choices=CATEGORIES, default='')
    agreement = models.IntegerField(default=0)
    disagreement = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_date"]

    def __str__(self):
        return self.title


class Comment(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_date"]

    def __str__(self):
        return f"Created by {self.author}"


class News(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, default='')
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_date"]


class Guides(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_date"]

    def __str__(self):
        return self.title

