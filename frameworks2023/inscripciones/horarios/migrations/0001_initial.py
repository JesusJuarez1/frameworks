# Generated by Django 4.1.7 on 2023-03-13 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('docentes', '0001_initial'),
        ('materias', '0001_initial'),
        ('salones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('clave', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Clave')),
                ('semestre', models.CharField(choices=[('1', '1er'), ('2', '2do'), ('3', '3er'), ('4', '4to'), ('5', '5to'), ('6', '6to'), ('7', '7mo'), ('8', '8vo'), ('9', '9no'), ('10', '10mo')], max_length=2, verbose_name='Semestre')),
                ('dia', models.CharField(choices=[('1', 'Lunes'), ('2', 'Martes'), ('3', 'Miércoles'), ('4', 'Jueves'), ('5', 'Viernes'), ('6', 'Sábado')], max_length=2, verbose_name='Dia')),
                ('hora', models.CharField(max_length=200, verbose_name='Hora')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='docentes.docente', verbose_name='Docente')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='materias.materia', verbose_name='Materia')),
                ('salon', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='salones.salon', verbose_name='Salon')),
            ],
        ),
    ]
