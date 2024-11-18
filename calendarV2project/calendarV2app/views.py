from django.shortcuts import render
from rest_framework import viewsets
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
    permission_classes = [AllowAny]

    def post(self, request):
        rut = request.data.get('rut')
        contraseña = request.data.get('contraseña')

        try:
            usuario = authenticate(request, username=rut, password=contraseña)
            if usuario:
                return JsonResponse({"message": "Inicio de sesión exitoso", "rut": usuario.rut}, status=200)
            else:
                return JsonResponse({"error": "Credenciales incorrectas"}, status=401)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)