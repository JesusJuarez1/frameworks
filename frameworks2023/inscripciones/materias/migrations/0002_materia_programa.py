# Generated by Django 4.1.7 on 2023-03-14 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programas', '0001_initial'),
        ('materias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='programa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='programas.programaacademico', verbose_name='Programa Academico'),
            preserve_default=False,
        ),
    ]