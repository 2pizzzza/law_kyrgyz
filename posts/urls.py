from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('posts/post', PostAPIView.as_view(), name='post-post'),
    path('posts/<int:pk>/', PostCreateUpdateDeleteAPIView.as_view(), name='post-pk'),
    path('comments/post', CommentAPIView.as_view(), name='comment-post'),
    path('comments/<int:pk>/', CommentCreateUpdateDeleteAPIView.as_view(), name='comment-pk'),
    path('news/post', NewsAPIView.as_view(), name='news-post'),
    path('news/<int:pk>/', NewsCreateUpdateDeleteAPIView.as_view(), name='news-pk'),
]

