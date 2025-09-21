# Gestor principal de tareas

from .tarea import Tarea
from .utils import filtrarPorPrioridad, filtrar_completadas, ordenarPorFecha

class GestorTareas:
    def __init__(self):
        self.tareas = []
    
    def agregarTarea(self, titulo, descripcion="", prioridad="media"):
        tarea = Tarea(titulo, descripcion, prioridad)
        self.tareas.append(tarea)
        return tarea