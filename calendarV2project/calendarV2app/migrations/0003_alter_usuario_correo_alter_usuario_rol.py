# Generated by Django 5.1.2 on 2024-11-18 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarV2app', '0002_usuario_last_login_usuario_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='correo',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.CharField(default='Estudiante', max_length=50),
        ),
    ]
