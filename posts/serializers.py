from rest_framework import serializers

from accounts.models import User

from .models import Comment, Guides, News, Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class GuidesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guides
        fields = "__all__"
