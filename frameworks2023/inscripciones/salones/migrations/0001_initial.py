# Generated by Django 4.1.7 on 2023-03-13 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Salon',
            fields=[
                ('clave', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Clave')),
                ('piso', models.SmallIntegerField(verbose_name='Piso')),
            ],
        ),
    ]