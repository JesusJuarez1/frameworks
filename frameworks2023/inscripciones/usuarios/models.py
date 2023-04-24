from django.db import models
from django.contrib.auth.models import User
from .validadores import rfc_validador, imagen_validador


class Docente(models.Model):
    matricula = models.CharField('Matrícula', max_length=50)
    rfc = models.CharField('R.F.C.', max_length=13, validators=[rfc_validador])
    nombre = models.CharField(max_length=150)
    apellido_paterno = models.CharField(max_length=150)
    apellido_materno = models.CharField(max_length=150)
    avatar = models.ImageField('Foto de perfil', upload_to='perfiles',validators=[imagen_validador])
    fecha_nacimiento = models.DateField()
    usuario = models.OneToOneField(User, verbose_name="Usuario", on_delete=models.CASCADE)

class Alumno(models.Model):
    matricula = models.CharField('Matrícula', max_length=50)
    apellido_paterno = models.CharField(max_length=150)
    avatar = models.ImageField('Foto de perfil', upload_to='perfiles')
    fecha_nacimiento = models.DateField()
    usuario = models.OneToOneField(User, verbose_name="Usuario", on_delete=models.CASCADE)
    programa = models.ForeignKey("programas.ProgramaAcademico", \
        verbose_name="Programa", on_delete=models.CASCADE)
