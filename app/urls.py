# configuracion de urls

from django.urls import path
from .views import home, galeria, ubicacion, register, admin, agregrar_insumos, listar_insumos, modificar_insumos, eliminar_insumos

urlpatterns = [
    path('', home, name="home"),
    path('galeria/', galeria, name="galeria"),
    path('agregar-insumos', agregrar_insumos, name="agregrar_insumos"),
    path('listar-insumos', listar_insumos, name="listar_insumos"),
    path('ubicacion/', ubicacion, name="ubicacion"),
    path('register/', register, name="register"),
    path('admin/', admin, name="admin"),
    path('modificar-insumos/<id>', modificar_insumos, name="modificar_insumos"),
    path('eliminar-insumos/<id>', eliminar_insumos, name="eliminar_insumos"),
]
