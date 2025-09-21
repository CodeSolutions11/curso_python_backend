from datetime import datetime

#print(datetime) # datetime.datetime
print(datetime.now()) # datetime.datetime

class Tarea:
    def __init__(self, titulo, descripcion="", prioridad="media"):
        self.titulo = titulo
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.completada = False
        self.fecha_creacion = datetime.now()
        self.fecha_completada = None
    
    def completar(self):
        self.completada=True
        self.fecha_completada=datetime.now()

    def __str__(self):
        estado = "✅" if self.completada else "o"
        return f"{estado} [{self.prioridad.upper()}] {self.titulo}"