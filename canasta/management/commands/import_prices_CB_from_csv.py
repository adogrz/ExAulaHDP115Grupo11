from django.core.management.base import BaseCommand
import csv
from canasta.models import CanastaBasicaAnual, CanastaBasicaMensual


class Command(BaseCommand):
    help = 'Importar datos de la canasta básica'

    def add_arguments(self, parser):
        parser.add_argument('anual_file', type=str)
        parser.add_argument('mensual_file', type=str)

    def handle(self, *args, **options):
        anual_file = options['anual_file']
        with open(anual_file) as f:
            reader = csv.reader(f)
            next(reader)  # Omitir encabezado
            for row in reader:
                if not CanastaBasicaAnual.objects.filter(anio=row[0]).exists():
                    anual_instance = CanastaBasicaAnual(anio=row[0],
                                                        precio_promedio=row[1],
                                                        inflacion=row[2])
                    anual_instance.save()
                else:
                    self.stderr.write(self.style.ERROR(
                        'Ya existe una instancia de CanastaBasicaAnual para el año ' + str(
                            row[0])))

        mensual_file = options['mensual_file']
        with open(mensual_file) as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                try:
                    anual_instance = CanastaBasicaAnual.objects.get(
                        anio=row[1])
                except CanastaBasicaAnual.DoesNotExist:
                    self.stderr.write(self.style.ERROR(
                        'No existe una instancia de CanastaBasicaAnual para el año ' + str(
                            row[0])))
                    continue

                mensual_instance = CanastaBasicaMensual()
                mensual_instance.precio = row[0]
                mensual_instance.anual = anual_instance
                mensual_instance.save()

        self.stdout.write(self.style.SUCCESS('Datos importados exitosamente!'))
