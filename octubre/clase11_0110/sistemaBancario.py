class SaldoInsufucienteError(Exception):
    def __init__(self, saldoActual, montoSolicitado):
        self.saldoActual = saldoActual
        self.montoSolicitado = montoSolicitado
        mensaje = f"Saldo insuficiente. Saldo: ${saldoActual}, Solicitado: ${montoSolicitado}"
        super().__init__(mensaje)


class CuentaBancaria:
    def __init__(self, saldoInicial=0):
        self.saldo = saldoInicial

    def retirar(self, monto):
        if monto > self.saldo:
            raise SaldoInsufucienteError(self.saldo, monto)
        self.saldo -= monto # self.saldo = self.saldo - monto
        return self.saldo

# Pruebas 
cuenta001 = CuentaBancaria(100)

try:
    cuenta001.retirar(30)
    cuenta001.retirar(150)
except SaldoInsufucienteError as e:
    print(f"Error: {e}")
    print(f"Saldo disponible: ${e.saldoActual}")
