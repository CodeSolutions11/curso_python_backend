from django.db import models
from django.contrib.auth.models import User

class Equipo(models.Model):
    LIGAS = [
        ('LALIGA', 'La Liga'),
        ('PREMIER', 'Premier League'),
        ('SERIEA', 'Serie A'),
        ('BUNDESLIGA', 'Bundesliga'),
        ('LIGUE1', 'Ligue 1'),    
    ]

    nombre = models.CharField(max_length=100)
    liga = models.CharField(max_length=20, choices=LIGAS)
    ciudad = models.CharField(max_length=100)
    fundado = models.IntegerField()
    estadio = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    escudo = models.URLField(default='https://example.com/default_escudo.png')
    descripcion = models.TextField(blank=True, null=True)
    partidos_jugados = models.IntegerField(default=0)
    victorias = models.IntegerField(default=0)
    empates = models.IntegerField(default=0)
    derrotas = models.IntegerField(default=0)
    goles_favor = models.IntegerField(default=0)
    goles_contra = models.IntegerField(default=0)

    @property
    def puntos(self):
        return self.victorias * 3 + self.empates
    
    @property
    def diferencia_goles(self):
        return self.goles_favor - self.goles_contra
    
    def __str__(self):
        return f"{self.nombre} ({self.liga})"
    
class Seguidor(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'equipo')

    def __str__(self):
        return f"{self.usuario.username} sigue a {self.equipo.nombre}"
    
class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return f"Comentario de {self.usuario.username} en {self.equipo.nombre}"