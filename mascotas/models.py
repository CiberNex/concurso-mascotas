from django.db import models


class Persona(models.Model):
    nombre = models.CharField(max_length=150)
    cedula = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nombre

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    persona = models.ForeignKey(
        Persona,
        on_delete=models.CASCADE,
        related_name='mascotas'
    )
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Participacion(models.Model):
    mascota = models.ForeignKey(
        Mascota,
        on_delete=models.CASCADE,
        related_name='participaciones'
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='participaciones'
    )
    foto = models.ImageField(upload_to='participaciones/')
    estado = models.CharField(max_length=20, default='pendiente')
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.mascota.nombre} - {self.categoria.nombre}"

class Voto(models.Model):
    persona = models.ForeignKey(
        Persona,
        on_delete=models.CASCADE,
        related_name='votos'
    )
    participacion = models.ForeignKey(
        Participacion,
        on_delete=models.CASCADE,
        related_name='votos'
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='votos'
    )
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['persona', 'categoria'],
                name='un_voto_por_persona_categoria'
            )
        ]

    def __str__(self):
        return f"{self.persona.nombre} - {self.participacion.mascota.nombre}"