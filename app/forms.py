from django import forms
from datetime import datetime
from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Insumos
from .validators import MaxFileSizeValidator

class InsumosForms(forms.ModelForm):
    nombre = forms.CharField(min_length=3, max_length=120)
    precio = forms.IntegerField(min_value=1)
    stock = forms.IntegerField(min_value=0)
    descripcion = forms.CharField(min_length=3, max_length=200, widget=forms.Textarea, required=False)
    imagen = forms.ImageField(required=False, validators=[MaxFileSizeValidator(max_file_size=2)])
    class Meta:
        model = Insumos
        fields = ["nombre", "precio", "stock", "descripcion", "imagen"]

class CustomUserCreationForm(UserCreationForm):
    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        if str(first_name).isalpha():
            return first_name
        raise ValidationError("Ingrese sólo letras")

    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"]
        if str(last_name).isalpha():
            return last_name
        raise ValidationError("Ingrese sólo letras")

    def clean_email(self):
        users = User.objects.all()
        email = self.cleaned_data["email"]

        for u in users:
            if u.email == email:
                raise ValidationError("Este mail ya está registrado")
        return email

    first_name = forms.CharField(min_length=3, max_length=80, required=True, label="Nombre")
    last_name = forms.CharField(min_length=3, max_length=80, required=True, label="Apellidos")
    email = forms.EmailField(required=True, label="Correo electrónico")

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]