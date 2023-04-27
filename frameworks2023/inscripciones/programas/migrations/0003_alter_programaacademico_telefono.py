# Generated by Django 4.1.6 on 2023-04-26 22:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programas', '0002_alter_programaacademico_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programaacademico',
            name='telefono',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator(code='telefono_invalido', message='El número de telefono tiene un formato inválido', regex='^\\d{10}$')], verbose_name='teléfono'),
        ),
    ]
