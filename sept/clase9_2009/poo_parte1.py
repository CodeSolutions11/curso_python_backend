class Estudiante:
    # Atributo/Propiedad de clase
    institucion = "Universidad CodeSolutions"

    def __init__(self, nombre, carrera):
        # Atributos de instancia (únicos para cada objeto)
        self.nombre = nombre
        self.carrera = carrera
        self.notas = []

    def agregarNota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        if self.notas:
            return sum(self.notas) / len(self.notas)
        return 0


estudiante1 = Estudiante("César", "Ingeniería")

#print(estudiante1.institucion, estudiante1.nombre, estudiante1.carrera)


class CuentaBancaria:
    def __init__(self, titular, saldoInicial=0):
        self.titular = titular          # Atributo Público
        self._saldo = saldoInicial       # Protegido (convención)
        self.__numeroCuenta = "123456" #Atributo Privado

    def getSaldo(self):
        return self._saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            return f"Depósito exitoso. Saldo: ${self._saldo}"
        return "Cantidad inválida"

    def retirar(self, cantidad):
        if 0 < cantidad <= self._saldo:
            self._saldo -= cantidad
            return f"Retiro exitoso. Saldo: ${self._saldo}"
        return "Fondos insuficientes"
    
    def getNumeroCuenta(self):
        """ Getter para acceder al número de cuenta """
        return self.__numeroCuenta

cuenta = CuentaBancaria("César", 1000)
#print(cuenta.titular, cuenta._saldo)
#print(cuenta.depositar(500))
#print(cuenta.retirar(800))
#print(cuenta.getNumeroCuenta())


# Herencia 
class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def hacerSonido(self):
        return "El animal hace un ruido"

    def dormir(self):
        return f"{self.nombre} está durmiendo"


# Clase hija (subclase)
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre, "Canino") # Llamar al constructor padre
        self.raza = raza

    def hacerSonido(self):
        return "Guau guau!!"

    def buscarPelota(self):
        return f"{self.nombre} está buscando la pelota"

class Gato(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre, "Felino")
        self.color = color

    def hacerSonido(self):
        return "Miau miau"

perro1 = Perro("Natsu", "Lobo Siberiano")
perro2 = Perro("Rex", "Labrador")
perro3 = Perro(None, "Pitbull")

#print(perro1.hacerSonido(), perro1.dormir())
#print(perro2.buscarPelota(), perro2.nombre)
#print(perro3.nombre, perro3.especie)


gato1 = Gato("bigotes", "Negro")
#print(gato1.nombre, gato1.especie, gato1.hacerSonido())


# Herencia Múltiple
class Volador:
    def volar(self):
        return "Estoy volando"

class Nadador:
    def nadar(self):
        return "Estoy nadando"

class Pato(Animal, Volador, Nadador):
    def __init__(self, nombre):
        super().__init__(nombre, "Ave")

    def hacerSonido(self):
        return "Cuac cuac"


pato1 = Pato("Donald")
print(pato1.nombre, pato1.especie)
print(pato1.volar())
print(pato1.nadar())
