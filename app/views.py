from django.shortcuts import render, redirect, get_object_or_404
from .models import Slider, Gallery, About_us, Insumos, Servicios
from .forms import CustomUserCreationForm, InsumosForms
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib import messages

# Create your views here.
def home(request):
    slider = Slider.objects.all()
    about_us = About_us.objects.last()
    servicios = Servicios.objects.all()

    data = {
        "slider":slider,
        "servicios":servicios,
        "mision": getattr(about_us, "mision"),
        "vision": getattr(about_us, "vision")
    }
    return render(request, 'app/home.html', data)

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],
                password=formulario.cleaned_data["password1"]
            )
            login(request, user)
            return redirect(to="home")
        data["form"] = formulario

    return render(request, 'registration/register.html', data)

def galeria(request):
    gallery = Gallery.objects.all()
    data = {
        "gallery":gallery
    }
    return render(request, 'app/galeria.html', data)

@permission_required('app.add_insumos')
def agregrar_insumos(request):
    data = {
        "form": InsumosForms(),
    }

    if request.method == 'POST':
        formulario = InsumosForms(data=request.POST, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardado correctamente")

        data["form"] = formulario

    return render(request, 'app/insumos/agregar.html', data)

@permission_required('app.view_insumos')
def listar_insumos(request):
    insumos = Insumos.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(insumos, 10)
        insumos = paginator.page(page)
    except:
        raise Http404

    data = {
        "entity": insumos,
        "paginator": paginator
    }

    return render(request, 'app/insumos/listar.html', data)

@permission_required('app.change_insumos')
def modificar_insumos(request, id):
    insumo = get_object_or_404(Insumos, id=id)

    data = {
        "form": InsumosForms(instance=insumo)
    }

    if request.method == 'POST':
        formulario = InsumosForms(data=request.POST, instance=insumo, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="listar_insumos")
        data["form"] = formulario

    return render(request, 'app/insumos/modificar.html', data)

@permission_required('app.delete_insumos')
def eliminar_insumos(request, id):
    insumo = get_object_or_404(Insumos, id=id)
    insumo.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="listar_insumos")

def ubicacion(request):
    return render(request, 'app/ubicacion.html')

def admin(request):
    return render(request, '/admin/')