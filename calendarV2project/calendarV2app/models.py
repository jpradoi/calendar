from django.db import models

class Usuario (models.Model):
    rut = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    contraseña = models.CharField(max_length=100)
    rol = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Asignatura(models.Model):
    asignatura_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

class UsuarioAsignatura(models.Model):
    rut = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    asignatura = models.ForeignKey('Asignatura', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('rut', 'asignatura')

class Horario(models.Model):
    DIA_CHOICES = [
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sábado', 'Sábado'),
        ('Domingo', 'Domingo'),
    ]
    horario_id = models.AutoField(primary_key=True)
    asignatura = models.ForeignKey('Asignatura', on_delete=models.CASCADE, null=True, blank=True, related_name="horarios")
    dia = models.CharField(max_length=20, choices=DIA_CHOICES)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"{self.asignatura.nombre} - {self.dia} ({self.hora_inicio} - {self.hora_fin})"

class Evento(models.Model):
    fecha_hora_evento = models.DateTimeField()
    asignatura = models.ForeignKey('Asignatura', on_delete=models.CASCADE)
    descripcion = models.TextField()

    class Meta:
        unique_together = ('fecha_hora_evento', 'asignatura')

class Calendario(models.Model):
    fechas = models.DateField()
