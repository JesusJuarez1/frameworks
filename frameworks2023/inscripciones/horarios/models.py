from django.db import models

SEMESTRES = [
    ('1', '1er'),
    ('2', '2do'),
    ('3', '3er'),
    ('4', '4to'),
    ('5', '5to'),
    ('6', '6to'),
    ('7', '7mo'),
    ('8', '8vo'),
    ('9', '9no'),
    ('10', '10mo'),
]

DIAS = [
    ('1', 'Lunes'),
    ('2', 'Martes'),
    ('3', 'Miércoles'),
    ('4', 'Jueves'),
    ('5', 'Viernes'),
    ('6', 'Sábado'),
]


class Horario(models.Model):
    clave = models.BigAutoField('Clave', primary_key=True)
    materia = models.ForeignKey("materias.Materia", verbose_name='Materia', on_delete=models.DO_NOTHING)
    docente = models.ForeignKey('docentes.Docente', verbose_name='Docente', on_delete=models.DO_NOTHING)
    semestre = models.CharField('Semestre' , max_length=2, choices=SEMESTRES)
    dia = models.CharField('Dia' , max_length=2, choices=DIAS)
    hora = models.CharField('Hora', max_length=200)
    salon = models.ForeignKey('salones.Salon', verbose_name='Salon', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.materia 
    
