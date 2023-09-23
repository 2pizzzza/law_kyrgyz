from rest_framework import serializers
from .models import Post, Comment, News
from accounts.models import User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(source='user.first_name')
    # author = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(), queryset=User.objects.all())
    # read_only_field = serializers.ReadOnlyField(source="author")

    class Meta:
        model = Post
        fields = ("author", "title", "content", "comments")


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = '__all__'
