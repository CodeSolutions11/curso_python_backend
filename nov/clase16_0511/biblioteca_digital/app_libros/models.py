from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    biografia = models.TextField() # Texto largo
    email = models.EmailField()
    sitio_web = models.URLField(blank=True, null=True) #opcional

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Editorial(models.Model):
    nombre = models.CharField(max_length=150)
    pais = models.CharField(max_length=50)
    fundada = models.IntegerField()
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    # Campos de texto 
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200, blank=True)
    descripcion = models.TextField()

    # Campos númericos 
    paginas = models.IntegerField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    # Campos de fecha y hora 
    fecha_publicacion = models.DateField()
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    fecha_actualizado = models.DateTimeField(auto_now=True)

    # Campos booleanos 
    disponible = models.BooleanField(default=True)
    es_bestseller = models.BooleanField(default=False)

    # Relaciones (las veremos en detalle mas adelante)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)

    idioma = models.CharField(max_length=50, default="Español")

    class Meta:
        ordering = ["-fecha_publicacion"] # Ornenar por fecha descendete
        verbose_name = "Libro"
        verbose_name_plural = "Libros"

    def __str__(self):
        return self.titulo


## Explicacion de cada campo:
# "CharField": Texto corto (maximo 200 carácteres)
# "DateField": Solo fecha (año/mes/dia)
# "IntegerField": Números enteros 
# "BooleanField": True/False 
# "__str__": Como se muestra el objeto cuando lo imprimes
