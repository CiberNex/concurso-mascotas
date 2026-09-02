from django.shortcuts import render, redirect
from .forms import RegistroMascotaForm
from .models import Persona, Mascota, Participacion


def registrar_mascota(request):
    if request.method == 'POST':
        form = RegistroMascotaForm(request.POST, request.FILES)

        if form.is_valid():
            persona, creada = Persona.objects.get_or_create(
                cedula=form.cleaned_data['cedula'],
                defaults={
                    'nombre': form.cleaned_data['nombre_persona']
                }
            )

            mascota = Mascota.objects.create(
                nombre=form.cleaned_data['nombre_mascota'],
                descripcion=form.cleaned_data['descripcion'],
                persona=persona
            )

            Participacion.objects.create(
                mascota=mascota,
                categoria=form.cleaned_data['categoria'],
                foto=form.cleaned_data['foto']
            )

            return redirect('registro_exitoso')

    else:
        form = RegistroMascotaForm()

    return render(
        request,
        'mascotas/registrar.html',
        {'form': form}
    )