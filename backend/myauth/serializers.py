from rest_framework import serializers
from myauth.models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password']

    


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        # Добавляем необходимую информацию о пользователе в ответ
        data['username'] = self.user.username
        data['email'] = self.user.email
        return data

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Добавляем необходимую информацию о пользователе в токен
        token['username'] = user.username
        token['email'] = user.email
        return token

    @classmethod
    def get_user_by_username(cls, username):
        try:
            return CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            return None

    @classmethod
    def get_user_by_email(cls, email):
        try:
            return CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return None

    def validate_username(self, value):
        user = self.get_user_by_username(value)
        if user is None:
            raise serializers.ValidationError("User does not exist")
        return value

    def validate_email(self, value):
        user = self.get_user_by_email(value)
        if user is None:
            raise serializers.ValidationError("User does not exist")
        return value
    
    
    
