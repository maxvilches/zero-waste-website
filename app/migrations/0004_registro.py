# Generated by Django 3.1.2 on 2020-10-08 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_producto_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=9)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('nombre_usuario', models.CharField(max_length=50)),
            ],
        ),
    ]
