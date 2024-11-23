from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.contrib.auth import authenticate
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

@api_view(['GET'])
def login_docente(request):
    rut = request.GET.get('rut')
    contraseña = request.GET.get('contraseña')

    try:
        user = Usuario.objects.get(rut=rut)
        if user.contraseña == contraseña:
            return JsonResponse({'message': 'Login successful', 'user_id': user.rut})
        else:
            return JsonResponse({'message': 'Invalid password'}, status=400)
    except Usuario.DoesNotExist:
        return JsonResponse({'message': 'User does not exist'}, status=404)