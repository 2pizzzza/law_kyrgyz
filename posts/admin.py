from django.contrib import admin
from .models import Post, Comment, News, Guides

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(News)
admin.site.register(Guides)
