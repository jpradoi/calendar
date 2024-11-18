from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, rut, password=None, **extra_fields):
        if not rut:
            raise ValueError('El usuario debe tener un rut')
        user = self.model(rut=rut, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, rut, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(rut, password, **extra_fields)

class Usuario(AbstractBaseUser):
    rut = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    contraseña = models.CharField(max_length=100)
    rol = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'rut'
    REQUIRED_FIELDS = ['nombre', 'correo']

    objects = UsuarioManager()

    def __str__(self):
        return self.rut

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
