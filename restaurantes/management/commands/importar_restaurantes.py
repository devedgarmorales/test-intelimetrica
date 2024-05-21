import csv
from django.core.management.base import BaseCommand
from restaurantes.models import Restaurante
from django.contrib.gis.geos import Point


class Command(BaseCommand):
    help = 'Importar restaurantes desde un archivo CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='La ruta al archivo CSV que se va a importar')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                restaurante, created = Restaurante.objects.update_or_create(
                    id=row[0],
                    defaults={
                        'clasificacion': row[1],
                        'nombre': row[2],
                        'sitio': row[3],
                        'correo': row[4],
                        'telefono': row[5],
                        'calle': row[6],
                        'ciudad': row[7],
                        'estado': row[8],
                        'lat': row[9],
                        'lng': row[10],
                        'ubicacion': Point(float(row[10]), float(row[9]))
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Restaurante "{restaurante.nombre}" creado'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'Restaurante "{restaurante.nombre}" actualizado'))
