from django.db import models

class UnidadAcademica(models.Model):
    nombre = models.CharField("Nombre", max_length=200)
    descripcion = models.TextField("Descripción")
    
    def __str__(self) -> str:
        return self.nombre