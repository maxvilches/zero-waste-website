# Generated by Django 3.1.2 on 2020-10-29 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20201027_2142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.TextField(max_length=30)),
            ],
        ),
    ]
