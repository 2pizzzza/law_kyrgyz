from django.db.models import Q
from rest_framework import status
from .serializers import PostSerializer, CommentSerializer, NewsSerializer, GuidesSerializer
from .models import Post, Comment, News, Guides
from rest_framework.views import APIView
from rest_framework.response import Response
from .blacklist import blacklist


def swear_words_validator(field_1, field_2, blacklist):
    str_1 = str(field_1)
    str_2 = str(field_2)
    for word in blacklist:
        if word.lower() in str_1.lower() or str_2.lower():
            if any(c.isupper() for c in word):
                return Response({'message': 'Пожалуйста не используйте маты'})


def authorization_validator(request):
    if not request.user.is_authenticated:
        return Response({'message': 'Пользователь не авторизован'})


def admin_validator(request, str_1):
    if request.user.is_superuser:
        return Response({'message': f'{str_1}'})


class PostAPIView(APIView):
    serializer_class = PostSerializer

    def get(self, request):
        agreement = request.GET.get('agreement')
        disagreement = request.GET.get('disagreement')
        category = request.GET.get('category')
        search_query = request.GET.get('search')
        posts = Post.objects.all()
        if agreement:
            posts = posts.filter(agreement=agreement)
        elif disagreement:
            posts = posts.filter(disagreement=disagreement)
        elif category:
            posts = posts.filte(category=category)

        if search_query:
            posts = posts.filter(
                Q(agreement__icontains=search_query) |
                Q(disagreement__icontains=search_query) |
                Q(category__icontains=search_query)
            )
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        authorization_validator(request)
        admin_validator(request, 'Администратор не может отправлять посты')
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        content = serializer.validated_data.get('content')
        title = serializer.validated_data.get('title')
        swear_words_validator(content, title, blacklist)
        serializer.validated_data['author'] = request.user
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PostRetrieveUpdateDeleteAPIView(APIView):
    serializer_class = PostSerializer

    def get(self, pk):
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response({'message': 'Пост не найден'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        authorization_validator(request)
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        authorization_validator(request)
        try:
            post = Post.objects.get(pk=pk)
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CommentAPIView(APIView):
    serializer_class = CommentSerializer

    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        authorization_validator(request)
        admin_validator(request, 'Администратор не может отправлять комментарии')
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        text = serializer.validated_data.get('text')
        swear_words_validator(text, None, blacklist)
        serializer.validated_data['author'] = request.user
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentRetrieveUpdateDeleteAPIView(APIView):
    serializer_class = CommentSerializer

    def get(self, pk):
        try:
            comment = Comment.objects.get(pk=pk)
            serializer = CommentSerializer(comment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Comment.DoesNotExist:
            return Response({'message': 'Комментарий не найден'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        authorization_validator(request)
        try:
            comment = Comment.objects.get(pk=pk)
            serializer = CommentSerializer(comment, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Comment.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        if not request.user.is_authenticated:
            return Response({'message': 'Пользователь не авторизован'})
        try:
            comment = Comment.objects.get(pk=pk)
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class NewsAPIView(APIView):
    serializer_class = NewsSerializer
    def get(self, request):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        authorization_validator(request)
        if not request.user.is_superuser:
            return Response({'message': 'Пользователь не может создавать новости'})

        serializer = NewsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['author'] = request.user
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class NewsRetrieveUpdateDeleteAPIView(APIView):
    serializer_class = NewsSerializer

    def get(self, pk):
        try:
            news = News.objects.get(pk=pk)
            serializer = NewsSerializer(news)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except News.DoesNotExist:
            return Response({'message': 'Новость не найдена'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        authorization_validator(request)
        try:
            news = News.objects.get(pk=pk)
            serializer = NewsSerializer(news, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except News.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        authorization_validator(request)
        try:
            news = News.objects.get(pk=pk)
            news.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except News.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class GuidesAPIView(APIView):
    serializer_class = GuidesSerializer
    def get(self, request):
        guides = Guides.objects.all()
        serializer = GuidesSerializer(guides, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        authorization_validator(request)
        if not request.user.is_superuser:
            return Response({'message': 'Пользователь не может создавать гайды'})
        serializer = GuidesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['author'] = request.user
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GuidesRetrieveUpdateDeleteAPIView(APIView):
    serializer_class = GuidesSerializer

    def get(self, pk):
        try:
            guides = Guides.objects.get(pk=pk)
            serializer = GuidesSerializer(guides)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Guides.DoesNotExist:
            return Response({'message': 'Гайд не найден'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        authorization_validator(request)
        try:
            guides = Guides.objects.get(pk=pk)
            serializer = GuidesSerializer(guides, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Guides.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        authorization_validator(request)
        try:
            guides = Guides.objects.get(pk=pk)
            guides.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Guides.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
