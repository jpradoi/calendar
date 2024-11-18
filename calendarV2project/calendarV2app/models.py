from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password

class UsuarioManager(BaseUserManager):
    def create_user(self, rut, nombre, correo, contraseña=None):
        if not rut:
            raise ValueError('El usuario debe tener un RUT')
        if not correo:
            raise ValueError('El usuario debe tener un correo electrónico')

        usuario = self.model(
            rut=rut,
            nombre=nombre,
            correo=self.normalize_email(correo),
        )
        usuario.set_password(contraseña)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, rut, nombre, correo, contraseña=None):
        usuario = self.create_user(rut, nombre, correo, contraseña)
        usuario.rol = 'Administrador'
        usuario.save(using=self._db)
        return usuario


class Usuario(AbstractBaseUser):
    rut = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100, unique=True)
    contraseña = models.CharField(max_length=100)
    rol = models.CharField(max_length=50, default='Estudiante')

    objects = UsuarioManager()

    USERNAME_FIELD = 'rut'  # Campo utilizado para autenticarse
    REQUIRED_FIELDS = ['nombre', 'correo']

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
