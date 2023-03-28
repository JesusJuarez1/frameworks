from django.db import models
from django.contrib.auth.models import User

class Docente(models.Model):
    matricula = models.CharField('Matricula', max_length=50)
    rfc = models.CharField('R.F.C.', max_length=13)
    nombre = models.CharField('Nombre', max_length=150)
    apellido_paterno = models.CharField(max_length=150)
    avatar = models.ImageField(upload_to='Foto sw perfil')
    fecha_nacimiento = models.DateField()
    usuario = models.OneToOneField(User, verbose_name='Usuario', on_delete=models.CASCADE)
    estado = models.ForeignKey("docentes.Estado", verbose_name="Estado", on_delete=models.DO_NOTHING)
    municipio = models.ForeignKey("docentes.Municipio", verbose_name="Municipio", on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.nombres +' '+ self.apellidos

class Estado(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
class Municipio(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.ForeignKey("docentes.Estado", verbose_name="Estado", on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.nombre