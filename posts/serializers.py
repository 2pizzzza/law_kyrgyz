from rest_framework import serializers

from accounts.models import User

from .models import Comment, News, Post


class PostSerializer(serializers.ModelSerializer):
    # author = serializers.StringRelatedField(source='user.first_name')
    # author = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(), queryset=User.objects.all())
    # author = serializers.ReadOnlyField(source="author")
    # agreements = serializers.ReadOnlyField(source="agreements")
    # disagreement = serializers.ReadOnlyField(source="disagreement")

    class Meta:
        model = Post
        # fields = ("author", "title", "content", "comments")
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"
