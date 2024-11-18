from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.hashers import make_password

class Usuario(AbstractBaseUser):
    rut = models.IntegerField(primary_key=True)
    rol = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    contraseña = models.CharField(max_length=100)

    def set_password(self, raw_password):
        self.contraseña = make_password(raw_password)
        self.save()

class Asignatura(models.Model):
    asignatura_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

class UsuarioAsignatura(models.Model):
    rut = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    asignatura = models.ForeignKey('Asignatura', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('rut', 'asignatura')

class Horario(models.Model):
    horario_id = models.AutoField(primary_key=True)
    asignatura = models.ForeignKey('Asignatura', on_delete=models.CASCADE)
    dia = models.CharField(max_length=20)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

class Evento(models.Model):
    fecha_hora_evento = models.DateTimeField()
    asignatura = models.ForeignKey('Asignatura', on_delete=models.CASCADE)
    descripcion = models.TextField()

    class Meta:
        unique_together = ('fecha_hora_evento', 'asignatura')

class Calendario(models.Model):
    fechas = models.DateField()
