# Generated by Django 4.1.6 on 2023-03-06 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materias', '0003_alter_materia_semestre'),
    ]

    operations = [
        migrations.CreateModel(
            name='MateriasPrecedentes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materia_actual', to='materias.materia', verbose_name='Materia')),
                ('materia_precedente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materia_precedente', to='materias.materia', verbose_name='Materia precedente')),
            ],
        ),
        migrations.DeleteModel(
            name='MateriaPrecedentes',
        ),
    ]
