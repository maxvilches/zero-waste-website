# Generated by Django 3.1.2 on 2020-10-24 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20201024_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='nombre',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
