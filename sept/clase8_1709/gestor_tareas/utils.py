# Utilidades para el gestor de tareas

def filtrarPorPrioridad(tareas, prioridad):
    # Filtra tareas por prioridad
    return [t for t in tareas if t.prioridad == prioridad]

def filtrar_completadas(tareas, completadas=True):
    return [t for t in tareas if t.completada == completadas ]

def ordenarPorFecha(tareas, descente=False):
    return sorted(tareas, key=lambda t: t.fecha_creacion, reverse=descente)