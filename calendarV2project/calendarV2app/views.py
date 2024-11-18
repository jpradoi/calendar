from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from .models import Usuario, Asignatura, UsuarioAsignatura, Horario, Evento, Calendario
from .serializers import (
    UsuarioSerializer,
    AsignaturaSerializer,
    UsuarioAsignaturaSerializer,
    HorarioSerializer,
    EventoSerializer,
    CalendarioSerializer
)

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class AsignaturaViewSet(viewsets.ModelViewSet):
    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSerializer

class UsuarioAsignaturaViewSet(viewsets.ModelViewSet):
    queryset = UsuarioAsignatura.objects.all()
    serializer_class = UsuarioAsignaturaSerializer

class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class CalendarioViewSet(viewsets.ModelViewSet):
    queryset = Calendario.objects.all()
    serializer_class = CalendarioSerializer

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        rut = request.data.get('rut')
        contraseña = request.data.get('contraseña')

        # Autenticar usuario
        usuario = authenticate(username=rut, password=contraseña)

        if usuario is not None:
            # Credenciales correctas
            return Response({"message": "Inicio de sesión exitoso"}, status=status.HTTP_200_OK)
        else:
            # Credenciales incorrectas
            return Response({"error": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)