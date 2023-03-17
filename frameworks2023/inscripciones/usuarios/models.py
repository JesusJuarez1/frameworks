from django.db import models
from django.contrib.auth.models import User
    
class Alumno(models.Model):
    matricula = models.CharField('Matricula', max_length=50)
    apellido_paterno = models.CharField(max_length=150)
    avatar = models.ImageField(upload_to='Foto sw perfil')
    fecha_nacimiento = models.DateField()
    usuario = models.OneToOneField(User, verbose_name="Usuario", on_delete=models.CASCADE)
    programa = models.ForeignKey("programas.ProgramaAcademico", verbose_name="Programa", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombres +' '+ self.apellidos