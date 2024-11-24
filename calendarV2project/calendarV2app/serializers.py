from rest_framework import serializers
from .models import Usuario, Asignatura, UsuarioAsignatura, Horario, Evento, Calendario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = ['horario_id', 'asignatura', 'dia', 'hora_inicio', 'hora_fin']

class AsignaturaSerializer(serializers.ModelSerializer):
    horarios = HorarioSerializer(many=True, required=False)

    class Meta:
        model = Asignatura
        fields = ['asignatura_id', 'nombre', 'horarios']

class UsuarioAsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioAsignatura
        fields = '__all__'

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'

class CalendarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendario
        fields = '__all__'