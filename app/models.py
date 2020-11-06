from django.db import models

# Create your models here.

class Slider(models.Model):
    nombre = models.CharField(max_length=10, null=True)
    imagen = models.ImageField(upload_to="slider")

    class Meta:
        verbose_name = "Foto del slider"
        verbose_name_plural = "Fotos del slider"

class Gallery(models.Model):
    nombre = models.CharField(max_length=10, null=True)
    imagen = models.ImageField(upload_to="gallery")

    class Meta:
        verbose_name = "Foto de la galería"
        verbose_name_plural = "Fotos de la galería"

class About_us(models.Model):
    mision = models.TextField(max_length=500)
    vision = models.TextField(max_length=500)

    class Meta:
        verbose_name = "Acerca de nosotros"
        verbose_name_plural = "Acerca de nosotros"

class Insumos(models.Model):
    nombre = models.CharField(max_length=120)
    precio = models.IntegerField()
    imagen = models.ImageField(null=True, blank=True, upload_to="insumos")
    descripcion = models.TextField(max_length=200, null=True, blank=True)
    stock = models.IntegerField()
    
    class Meta:
        verbose_name = "Insumo"
        verbose_name_plural = "Insumos"

class Servicios(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField(max_length=200)
    imagen = models.ImageField(null=True, blank=True, upload_to="servicios")
    
    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
