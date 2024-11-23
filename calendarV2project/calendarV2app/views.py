import datetime
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
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
    
@api_view(['GET'])
def class_schedule(request):
    # Get today's day name in Spanish (e.g., 'Lunes', 'Martes', etc.)
    today = timezone.localtime(timezone.now())
    current_day = today.strftime('%A')  # Get day in English (e.g., 'Monday')

    # Map English day names to Spanish
    day_translation = {
        'Monday': 'Lunes',
        'Tuesday': 'Martes',
        'Wednesday': 'Miércoles',
        'Thursday': 'Jueves',
        'Friday': 'Viernes',
        'Saturday': 'Sábado',
        'Sunday': 'Domingo'
    }

    spanish_day = day_translation.get(current_day, '')

    if not spanish_day:
        return Response({'error': 'Unable to identify today\'s day.'}, status=status.HTTP_400_BAD_REQUEST)

    # Get all Asignaturas that have a Horario for the current day
    clases_hoy = Asignatura.objects.filter(
        horarios__dia=spanish_day
    ).distinct()

    # Serialize the data
    serializer = AsignaturaSerializer(clases_hoy, many=True)

    return Response(serializer.data)