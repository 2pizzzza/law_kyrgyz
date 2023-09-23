from django.contrib.auth import logout
from django.shortcuts import render

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import UserSerializer

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