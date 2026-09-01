from django.contrib import admin
from .models import Persona, Mascota, Categoria, Participacion, Voto


admin.site.register(Persona)
admin.site.register(Mascota)
admin.site.register(Categoria)
admin.site.register(Participacion)
admin.site.register(Voto)