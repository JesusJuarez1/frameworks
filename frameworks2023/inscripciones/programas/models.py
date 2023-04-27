from django.db import models
from .validadores import telefono_validador

class ProgramaAcademico(models.Model):
    clave = models.BigAutoField('Clave', primary_key=True)
    nombre = models.CharField("Nombre", max_length=200)
    latitud = models.CharField(max_length=50)
    longitud = models.CharField(max_length=50)
    telefono = models.CharField('teléfono', max_length=10, blank=True, null=True, validators=[telefono_validador])
    unidad_academica = models.ForeignKey("unidades_academicas.UnidadAcademica", \
        verbose_name='Unidad Académica', on_delete=models.DO_NOTHING)
    
    def __str__(self) -> str:
        return self.nombre