from django.shortcuts import render, redirect, get_object_or_404

from .forms import RegistroMascotaForm
from .models import Persona, Mascota, Categoria, Participacion, Voto


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


def votar(request, participacion_id):
    participacion = get_object_or_404(
        Participacion,
        id=participacion_id,
        estado='aprobada'
    )

    if request.method == 'POST':
        cedula = request.POST.get('cedula')

        try:
            persona = Persona.objects.get(cedula=cedula)
        except Persona.DoesNotExist:
            return render(
                request,
                'mascotas/votar.html',
                {
                    'participacion': participacion,
                    'error': 'La cédula no está registrada.'
                }
            )

        ya_voto = Voto.objects.filter(
            persona=persona,
            categoria=participacion.categoria
        ).exists()

        if ya_voto:
            return render(
                request,
                'mascotas/votar.html',
                {
                    'participacion': participacion,
                    'error': 'Ya has votado en esta categoría.'
                }
            )

        Voto.objects.create(
            persona=persona,
            participacion=participacion,
            categoria=participacion.categoria
        )

        return render(
            request,
            'mascotas/votar.html',
            {
                'participacion': participacion,
                'mensaje': '¡Tu voto ha sido registrado!'
            }
        )

    return render(
        request,
        'mascotas/votar.html',
        {
            'participacion': participacion
        }
    )


def galeria(request, categoria_id):
    categoria = get_object_or_404(
        Categoria,
        id=categoria_id
    )

    participaciones = Participacion.objects.filter(
        categoria=categoria,
        estado='aprobada'
    ).order_by('-fecha_registro')

    return render(
        request,
        'mascotas/galeria.html',
        {
            'categoria': categoria,
            'participaciones': participaciones
        }
    )
def registro_exitoso(request):
    return render(
        request,
        'mascotas/registro_exitoso.html'
    )
def inicio(request):
    return render(
        request,
        'mascotas/index.html'
    )
def evento(request):
    return render(
        request,
        'mascotas/evento.html'
    )