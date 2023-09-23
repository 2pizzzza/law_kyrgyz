from rest_framework import serializers
from .models import Post, Comment, News


class PostSerializer(serializers.ModelSerializer):

    read_only_field = serializers.ReadOnlyField(source="author")

    class Meta:
        model = Post
        # exclude = ("agreement", "disagreement", "answer")
        fields = ("title", "content", "comments", "read_only_field")


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = '__all__'
