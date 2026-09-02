from django import forms
from .models import Persona, Mascota, Participacion


class RegistroMascotaForm(forms.Form):
    nombre_persona = forms.CharField(
        max_length=150,
        label='Nombre completo'
    )

    cedula = forms.CharField(
        max_length=20,
        label='Cédula'
    )

    nombre_mascota = forms.CharField(
        max_length=100,
        label='Nombre de la mascota'
    )

    descripcion = forms.CharField(
        widget=forms.Textarea,
        label='Descripción'
    )

    categoria = forms.ModelChoiceField(
        queryset=None,
        label='Categoría'
    )

    foto = forms.ImageField(
        label='Fotografía'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from .models import Categoria
        self.fields['categoria'].queryset = Categoria.objects.all()