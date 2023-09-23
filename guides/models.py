from django.db import models


def upload_to(instance, filename):
    return "images/{filename}".format(filename=filename)


TYPES = (
    ("бизнес", "бизнес"),
    ("медицина", "медицина"),
    ("образование", "образование"),
    ("экология", "экология"),
    ("суды", "суды"),
    ("религия", "религия"),
)


class Guide(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    guide_type = models.CharField(choices=TYPES, max_length=100, blank=True)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_date"]

    def __str__(self):
        return self.title
