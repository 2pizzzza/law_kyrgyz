from django.db import models


def upload_to(instance, filename):
    return "images/{filename}".format(filename=filename)


class Guide(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_date"]

    def __str__(self):
        return self.title
