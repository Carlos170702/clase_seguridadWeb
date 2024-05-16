from rest_framework.serializers import ModelSerializer
from apps.users.models import UserModel
from rest_framework import serializers
import re


class UserSerializer(ModelSerializer):
    email = serializers.EmailField(error_messages={
        'invalid': 'Correo no valido'
    })

    class Meta:
        model = UserModel
        fields = '__all__'

    def validate_username(self, value):
        if UserModel.objects.filter(username=value).exists():
            raise serializers.ValidationError("Nombre de usuario ya existe")
        return value

    def validate_email(self, value):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if UserModel.objects.filter(email=value).exists():
            raise serializers.ValidationError("Correo ya existe")

        if not re.match(pattern, value):
            raise serializers.ValidationError("Correo no valido")
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError(
                "La contraseña debe tener al menos 8 caracteres")

        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError(
                "La contraseña debe contener al menos un número")

        if not any(char.isupper() for char in value):
            raise serializers.ValidationError(
                "La contraseña debe contener al menos una letra mayúscula")

        if not any(char in ['$', '@', '#', '%', '&', '*'] for char in value):
            raise serializers.ValidationError(
                "La contraseña debe contener al menos un carácter especial")

        return value
