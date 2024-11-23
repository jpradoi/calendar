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
def get_asignaturas_para_dia(request):
    dia = request.query_params.get('dia', None)
    mes = request.query_params.get('mes', None)
    
    if dia and mes:
        # Suponiendo que el mes es un nombre como "Enero", "Febrero", etc.
        mes_num = datetime.strptime(mes, '%B').month  # Convierte el nombre del mes a número (Enero -> 1, etc.)
        
        # Aquí puedes buscar las asignaturas que tengan horarios en ese día y mes
        asignaturas = Asignatura.objects.filter(horarios__dia=dia, horarios__asignatura__mes=mes_num)
        
        # Devuelves las asignaturas junto con los horarios
        resultado = []
        for asignatura in asignaturas:
            horarios = Horario.objects.filter(asignatura=asignatura, dia=dia)
            resultado.append({
                'asignatura_id': asignatura.asignatura_id,
                'nombre': asignatura.nombre,
                'horarios': [{'horario_id': h.horario_id, 'dia': h.dia, 'hora_inicio': h.hora_inicio, 'hora_fin': h.hora_fin} for h in horarios]
            })
        
        return Response(resultado)
    else:
        return Response({"error": "Faltan parámetros"}, status=400)