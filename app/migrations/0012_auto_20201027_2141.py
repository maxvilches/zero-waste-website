# Generated by Django 3.1.2 on 2020-10-28 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20201025_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insumos',
            name='descripcion',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]