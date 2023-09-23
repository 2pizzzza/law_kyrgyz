# from django.contrib.auth.models import User
from accounts.models import User
from django.db import models


class Post(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
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


class News(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, editable=True)
    content = models.TextField()
    comments = models.ManyToManyField(Comment, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_date"]
