from django.db import models

class Salon(models.Model):
    clave = models.BigAutoField('Clave', primary_key=True)
    piso = models.SmallIntegerField('Piso')
    
    def __str__(self):
        return str(self.clave)