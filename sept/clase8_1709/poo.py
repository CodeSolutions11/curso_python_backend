class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        return f"Hola, soy {self.nombre}"
    
    
# un metodo es una funcion que pertenece a un objeto
# una propiedad es una variable que pertenece a un objeto

# Crear objeto (instancia)    
persona1 = Persona("Cesar", 25)
persona2 = Persona("Carlos", 30)

# print(persona1.nombre, persona1.edad, persona1.saludar())
# print(persona2.nombre, persona2.edad, persona2.saludar())

class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0
    
    def acelerar(self):
        self.velocidad += 100 # self.velocidad = self.velocidad + 10
        return f"Acelerando... Velocidad: {self.velocidad} km/h"
    
coche1 = Coche("Toyota", "Corolla")
coche2 = Coche("Honda", "Civic")

print(coche1)

# print(coche1.modelo, coche1.marca, coche1.acelerar())
# print(coche2.modelo, coche2.marca, coche2.acelerar())

class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"{self.titulo} por {self.autor}"
    
    def __len__(self):
        return self.paginas
    
    def __eq__(self, otro):
        # Define como comparar objetos con == 
        return self.titulo == otro.titulo and self.autor == otro.autor
    
libro1 =  Libro("1984", "Geaorge Orwell", 328)
libro2 =  Libro("1984", "Clean Code", 200)
libro3 =  Libro("1984", "Clean Code", 200)

print(libro1)
print(libro1.__eq__(libro3))
print(len(libro1)) # 328
print(libro1 == libro2)
print(libro2 == libro3)