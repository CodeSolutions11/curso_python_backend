# Ejemplo práctico
#

class Vehiculo:
    def __init__(self, marca, modelo, year):
        self.marca = marca
        self.modelo = modelo
        self.year = year
        self._km = 0

    def arrancar(self):
        return f"{self.marca} {self.modelo} arrancando..."

    def conducir(self, km):
        self._km += km 
        return f"Conducido {km} km. Total: {self._km} km"

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.year})"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, year, puertas):
        super().__init__(marca, modelo, year)
        self.puertas = puertas

    def abrirMaletero(self):
        return "Maletero Abierto"

class Moto(Vehiculo):
    def __init__(self, marca, modelo, year, cilindrada):
        super().__init__(marca, modelo, year)
        self.cilindrada = cilindrada

    def hacerCaballito(self):
        return "Haciendo caballito!!!"

# Uso del sistema
#
carro1 = Coche("Toyota", "Corrolla", 2022, 4)
moto = Moto("Honda", "CBR", 2021, 1000)

print(carro1.marca ,carro1.arrancar(), carro1.abrirMaletero(), carro1.conducir(50))
print(moto.marca, moto.arrancar(), moto.conducir(70), moto.hacerCaballito())
