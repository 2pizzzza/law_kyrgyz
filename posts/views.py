from django.shortcuts import render
from rest_framework import permissions, status
from .serializers import PostSerializer, CommentSerializer, NewsSerializer
from .models import Post, Comment, News
from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class PostUpvoteView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.agreement += 1
        instance.save()
        return instance


class PostDownvoteView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.disagreement += 1
        instance.save()
        return instance


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticated]


class PostRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticated]


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = [IsAuthenticated]


class CommentRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = [IsAuthenticated]


class VoteView(generics.CreateAPIView):
    pass


class PostAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def post(self, request):
        if request.user.is_superuser:
            return Response({'message': 'Администратор не может отправлять посты'})
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['author'] = request.user
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PostCreateUpdateDeleteAPIView(APIView):
    serializer_class = PostSerializer

    def get(self, pk):
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response({'message': 'Пост не найден'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, pk):
        try:
            post = Post.objects.get(pk=pk)
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CommentAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer

    def post(self, request):
        if request.user.is_superuser:
            return Response({'message': 'Администратор не может отправлять комментарии'})
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['author'] = request.user
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentCreateUpdateDeleteAPIView(APIView):
    serializer_class = CommentSerializer

    def get(self, pk):
        try:
            comment = Comment.objects.get(pk=pk)
            serializer = CommentSerializer(comment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Comment.DoesNotExist:
            return Response({'message': 'Комментарий не найден'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            comment = Comment.objects.get(pk=pk)
            serializer = CommentSerializer(comment, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Comment.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, pk):
        try:
            comment = Comment.objects.get(pk=pk)
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class NewsAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NewsSerializer

    def post(self, request):
        if not request.user.is_superuser:
            return Response({'message': 'Пользователь не может создавать новости'})
        serializer = NewsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['author'] = request.user
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class NewsCreateUpdateDeleteAPIView(APIView):
    serializer_class = NewsSerializer

    def get(self, pk):
        try:
            news = News.objects.get(pk=pk)
            serializer = NewsSerializer(news)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except News.DoesNotExist:
            return Response({'message': 'Комментарий не найден'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            news = News.objects.get(pk=pk)
            serializer = CommentSerializer(news, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except News.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, pk):
        try:
            news = News.objects.get(pk=pk)
            news.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except News.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
