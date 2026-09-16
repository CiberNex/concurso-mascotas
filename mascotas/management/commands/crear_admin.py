import os

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Crea el usuario administrador si no existe'

    def handle(self, *args, **options):
        User = get_user_model()

        username = os.environ.get('ADMIN_USERNAME')
        email = os.environ.get('ADMIN_EMAIL')
        password = os.environ.get('ADMIN_PASSWORD')

        if not username or not password:
            self.stdout.write(
                'Variables de administrador no configuradas. '
                'Se omite la creación.'
            )
            return

        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                'email': email or '',
                'is_staff': True,
                'is_superuser': True,
            }
        )

        if created:
            user.set_password(password)
            user.save()

            self.stdout.write(
                self.style.SUCCESS(
                    f'Administrador "{username}" creado correctamente.'
                )
            )
        else:
            self.stdout.write(
                self.style.WARNING(
                    f'El administrador "{username}" ya existe.'
                )
            )