from django.contrib import admin
from .models import Slider, Gallery, About_us, Insumos, Servicios

# Register your models here.

class SliderAdmin(admin.ModelAdmin):
    list_display = ["nombre", "imagen"]
    search_fields = ["nombre"]
    list_per_page = 10
    list_editable = ["imagen"]

class GalleryAdmin(admin.ModelAdmin):
    list_display = ["nombre", "imagen"]
    search_fields = ["nombre"]
    list_per_page = 10
    list_editable = ["imagen"]

class About_us_Admin(admin.ModelAdmin):
    list_display = ["mision", "vision"]
    search_fields = ["mision", "vision"]
    list_per_page = 10

class Insumos_Admin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "imagen", "descripcion", "stock"]
    search_fields = ["nombre"]
    list_per_page = 10

class Servicios_Admin(admin.ModelAdmin):
    list_display = ["nombre", "descripcion", "imagen"]
    search_fields = ["nombre"]
    list_per_page = 10

admin.site.register(Slider, SliderAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(About_us, About_us_Admin)
admin.site.register(Insumos, Insumos_Admin)
admin.site.register(Servicios, Servicios_Admin)

admin.site.site_header = 'Administración Carwash'
admin.site.site_title = 'Carwash'
admin.site.index_title = 'Sitio administrativo Carwash'
