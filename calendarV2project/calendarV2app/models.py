from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, rut, nombre, correo, rol, password=None):
        if not rut:
            raise ValueError("El usuario debe tener un RUT")
        if not correo:
            raise ValueError("El usuario debe tener un correo")

        usuario = self.model(
            rut=rut,
            nombre=nombre,
            correo=self.normalize_email(correo),
            rol=rol,
        )
        usuario.set_password(password)  # Hashear la contraseña
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, rut, nombre, correo, rol, password):
        usuario = self.create_user(
            rut=rut,
            nombre=nombre,
            correo=correo,
            rol=rol,
            password=password,
        )
        usuario.is_admin = True
        usuario.save(using=self._db)
        return usuario


class Usuario(AbstractBaseUser):
    rut = models.IntegerField(unique=True, primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100, unique=True)
    rol = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = "rut"
    REQUIRED_FIELDS = ["nombre", "correo", "rol"]

    def __str__(self):
        return f"{self.nombre} ({self.rut})"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

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
