from django.urls import path
from .views import PostAPIView, PostCreateUpdateDeleteAPIView
from . import views

urlpatterns = [
    path('posts/create', views.PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', views.PostRetrieveUpdateDeleteView.as_view(), name='post-detail'),
    path('comments/', views.CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', views.CommentRetrieveUpdateDeleteView.as_view(), name='comment-detail'),
    path('posts/', PostAPIView.as_view(), name='post'),
    path('posts/<int:pk>/', PostCreateUpdateDeleteAPIView.as_view(), name='post'),
    path('posts/<int:pk>/upvote/', views.PostUpvoteView.as_view(), name='post-upvote'),
    path('posts/<int:pk>/downvote/', views.PostDownvoteView.as_view(), name='post-downvote'),
]

