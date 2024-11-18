from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login
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

@api_view(['POST'])
def login_usuario(request):
    # Obtener las credenciales del cuerpo de la solicitud
    rut = request.data.get('rut')
    password = request.data.get('password')

    # Intentar autenticar al usuario
    user = authenticate(request, username=rut, password=password)

    if user is not None:
        # Si el usuario es autenticado correctamente, respondemos con un mensaje de éxito
        return Response({"message": "Login exitoso"}, status=status.HTTP_200_OK)
    else:
        # Si las credenciales son incorrectas, respondemos con un error
        return Response({"message": "Credenciales incorrectas"}, status=status.HTTP_400_BAD_REQUEST)