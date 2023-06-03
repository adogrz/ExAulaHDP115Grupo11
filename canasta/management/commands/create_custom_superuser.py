import argparse
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Crea un nuevo superusuario personalizado'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Nombre de usuario')
        parser.add_argument('email', type=str, help='Correo electrónico')
        parser.add_argument('--password', type=str, help='Contraseña',
                            required=True)

    def handle(self, *args, **options):
        User.objects.create_superuser(
            username=options['username'],
            email=options['email'],
            password=options['password'],
        )
        self.stdout.write(
            self.style.SUCCESS('Superusuario creado satisfactoriamente'))
