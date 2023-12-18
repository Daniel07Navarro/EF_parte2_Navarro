from django.db import models

# Create your models here.
class Docente(models.Model):
    iddocente = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=5,unique=True)
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    dni = models.CharField(max_length=8)
    fecha_nacimiento = models.CharField(max_length=100)
    fecha_registro = models.CharField(max_length=100)
    estado = models.BooleanField()