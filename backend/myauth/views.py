from myauth.models import CustomUser
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.response import Response
from rest_framework import status
from myauth.serializers import CustomTokenObtainPairSerializer, CustomUserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password


class RegistrationView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if CustomUser.objects.filter(username=username).exists():
            return Response({'error': 'Имя пользователя уже используется'}, status=status.HTTP_400_BAD_REQUEST)

        # Используйте make_password для хеширования пароля
        hashed_password = make_password(password)

        user = CustomUser.objects.create_user(username=username, password=hashed_password, email=email)
        return Response({'message': 'Пользователь успешно зарегистрирован'}, status=status.HTTP_201_CREATED)
    
    

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    
class CustomUserListView(APIView):
    def get(self, request):
        # Получаем всех пользователей
        users = CustomUser.objects.all()
        # Сериализуем данные пользователей
        serializer = CustomUserSerializer(users, many=True)
        # Возвращаем сериализованные данные пользователей в ответе
        return Response(serializer.data)