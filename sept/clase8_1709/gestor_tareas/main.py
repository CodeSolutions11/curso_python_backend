from . import GestorTareas
print(GestorTareas)

def main():
    gestor = GestorTareas()
    
    #Agregar Tarea
    gestor.agregarTarea("Estudiar Python")

    print("Creacion de tareas")

if __name__ == "__main__":
    main()