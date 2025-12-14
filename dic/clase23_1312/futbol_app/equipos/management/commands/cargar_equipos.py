from django.core.management.base import BaseCommand
from equipos.models import Equipo

class Command(BaseCommand):
    help = 'Carga equipos de fútbol iniciales en la base de datos'

    def handle(self, *args, **kwargs):
        equipos_data = [
            {
                'nombre': 'FC Barcelona',
                'liga': 'LALIGA',
                'ciudad': 'Barcelona',
                'fundado': 1899,
                'estadio': 'Camp Nou',
                'capacidad': 99354,
                'escudo': 'https://example.com/barcelona_escudo.png',
                'descripcion': 'El FC Barcelona es uno de los clubes más exitosos de España y del mundo.'
            },
            {
                'nombre': 'Manchester United',
                'liga': 'PREMIER',
                'ciudad': 'Manchester',
                'fundado': 1878,
                'estadio': 'Old Trafford',
                'capacidad': 74879,
                'escudo': 'https://example.com/manutd_escudo.png',
                'descripcion': 'Manchester United es uno de los clubes más populares y exitosos de Inglaterra.'
            },
            {
                'nombre': 'Juventus',
                'liga': 'SERIEA',
                'ciudad': 'Turín',
                'fundado': 1897,
                'estadio': 'Allianz Stadium',
                'capacidad': 41507,
                'escudo': 'https://example.com/juventus_escudo.png',
                'descripcion': 'La Juventus es el club más exitoso de Italia con numerosos títulos nacionales e internacionales.'
            },
        ]

        for equipo_data in equipos_data:
            equipo, created = Equipo.objects.get_or_create(
                nombre=equipo_data['nombre'],
                defaults=equipo_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Equipo "{equipo.nombre}" creado exitosamente.'))
            else:
                self.stdout.write(self.style.WARNING(f'El equipo "{equipo.nombre}" ya existe.'))
        self.stdout.write(self.style.SUCCESS('Carga de equipos completada.'))