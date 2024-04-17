from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializer import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

# Create your views here.

class CreateUserView(generics.CreateAPIView):
    # Consulta para obtener todos los objetos del modelo User
    queryset = User.objects.all()

    # Clase de serializador a utilizar para la creación de usuarios
    serializer_class = UserSerializer

    # Clases de permisos para esta vista
    # AllowAny permite que cualquier persona cree un usuario sin autenticación
    permission_classes = [AllowAny]

class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
      user = self.request.user
      return Note.objects.filter(author=user)
    
    def perform_create(self, serializer):
      if serializer.is_valid():
          serializer.save(author=self.request.user)
      else:
          print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)