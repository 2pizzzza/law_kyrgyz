from django.contrib.auth import logout

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User, Notification
from .serializers import UserSerializer, NotificationsSerializer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class RegistrationAPIView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        return Response({
            'message': 'User registered successfully',
            'access_token': access_token,
            'refresh_token': refresh_token
        }, status=status.HTTP_201_CREATED)


class UserLoginAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        data = request.data
        email = data.get('email')
        password = data.get('password')
        user = User.objects.filter(email=email).first()

        if user is None:
            return Response({'error': 'User not found'}, status=400)

        if not user.check_password(password):
            return Response({'error': 'Invalid password'}, status=400)

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)
        return Response({'access_token': access_token, 'refresh_token': refresh_token
        }, status=status.HTTP_201_CREATED)


class UserLogoutAPIView(APIView):
    def post(self, request):
        # Log the user out
        logout(request)
        return Response({'message': 'User logged out successfully'}, status=status.HTTP_200_OK)


class NotificationsAPIView(APIView):
    serializer_class = NotificationsSerializer

    def get(self, request):
        notifications = Notification.objects.all()
        serializer = NotificationsSerializer(notifications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if not request.user.is_superuser:
            return Response({'message': 'Запрещено'})
        serializer = NotificationsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class NotificationsRetrieveUpdateDeleteAPIView(APIView):
    serializer_class = NotificationsSerializer

    def get(self, pk):
        try:
            notification = Notification.objects.get(pk=pk)
            serializer = NotificationsSerializer(notification)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Notification.DoesNotExist:
            return Response({'message': 'У вас нет уведомлений'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        if not request.user.is_superuser:
            return Response({'message': 'Запрещено'})
        try:
            notification = Notification.objects.get(pk=pk)
            serializer = NotificationsSerializer(notification, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Notification.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        if not request.user.is_superuser:
            return Response({'message': 'Запрещено'})
        try:
            guides = Notification.objects.get(pk=pk)
            guides.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Notification.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)