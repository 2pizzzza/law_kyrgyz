from django.urls import path
from .views import *

urlpatterns = [
    path('posts/post/', PostAPIView.as_view(), name='post-post'),
    path('posts/<int:pk>/', PostRetrieveUpdateDeleteAPIView.as_view(), name='post-pk'),
    path('comments/post/', CommentAPIView.as_view(), name='comment-post'),
    path('comments/<int:pk>/', CommentRetrieveUpdateDeleteAPIView.as_view(), name='comment-pk'),
    path('news/post/', NewsAPIView.as_view(), name='news-post'),
    path('news/<int:pk>/', NewsRetrieveUpdateDeleteAPIView.as_view(), name='news-pk'),
    path('guides/post/', GuidesAPIView.as_view(), name='guides-post'),
    path('guides/<int:pk>/', GuidesRetrieveUpdateDeleteAPIView.as_view(), name='guides-pk'),
]

