from django.db import models

from accounts.models import User

CATEGORIES = (
    ("Образование", "Образование"),
    ("Медицина", "Медицина"),
    ("Природа", "Природа"),
    ("Судебная", "Судебная"),
    ("Бизнес", "Бизнес"),
    ("СМИ", "СМИ"),
)


def upload_to(instance, filename):
    return "images/{filename}".format(filename=filename)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
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
    title = models.CharField(max_length=100, default="")
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, editable=True)
    content = models.TextField()
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    comments = models.ManyToManyField(Comment, null=True)
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
