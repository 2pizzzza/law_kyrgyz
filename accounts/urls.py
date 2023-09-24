from django.urls import path
from .views import RegistrationAPIView, UserLoginAPIView, UserLogoutAPIView, NotificationsAPIView, NotificationsRetrieveUpdateDeleteAPIView

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('logout/', UserLogoutAPIView.as_view(), name='logout'),
    path('notifications/post', NotificationsAPIView.as_view(), name='notification-post'),
    path('notifications/<int:pk>', NotificationsRetrieveUpdateDeleteAPIView.as_view(), name='notification-act')
]
