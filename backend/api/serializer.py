from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # Define el modelo con el que se trabajará (User en este caso)
        model = User

        # Campos que se incluirán en la representación serializada
        fields = ["id", "username", "password"]

        # Configuración adicional para el campo de contraseña.  
        #La contraseña solo se enviará al crear un usuario y no se mostrará en las respuestas.
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        # Crea un nuevo usuario utilizando los datos validados
        user = User.objects.create_user(**validated_data)
        return user

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model= Note
        fields = ["id","title","content","created_at","author"]
        extra_kwargs = {"author":{"read_only": True}}
        