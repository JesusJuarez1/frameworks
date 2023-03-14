from django.db import models

class Docente(models.Model):
    matricula = models.CharField('Matricula', primary_key=True, max_length=8)
    nombres = models.CharField('Nombres', max_length=150)
    apellidos = models.CharField('Apellidos', max_length=150)
    
    def __str__(self):
        return self.nombres +' '+ self.apellidos