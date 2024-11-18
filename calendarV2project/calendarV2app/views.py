from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
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
    def post(self, request, *args,**kwargs):
        rut = request.data.get('rut')
        contraseña = request.data.get('contraseña')

        try:
            usuario = get_user_model().objects.get(rut=rut)

            if not check_password(contraseña, usuario.contraseña):
                return Response({"error": "Credenciales inválidas"}, status=status.HTTP_400_BAD_REQUEST)
            
            refresh = RefreshToken.for_user(usuario)
            access_token = str(refresh.access_token)
            return Response({"token": access_token}, status=status.HTTP_200_OK)
        
        except get_user_model().DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_400_BAD_REQUEST)