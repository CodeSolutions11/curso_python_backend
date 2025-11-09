from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal


class CuentaBancaria(models.Model):
    """
    Modelo que representa una cuenta bancaria en el sistema
    Principios aplicados: 
    - Precisión decimal absoluta
    - Inmutabilidad de datos críticos
    - Trazabilidad completa
    """

    TIPOS_CUENTA = [
        ('ahorros', "Cuenta de Ahorros"),
        ('corriente', "Cuenta Corriente"),
        ('inversion', "Cuenta de Inversión"),
        ('crediro', "Cuenta de Crédito"),
    ]

    ESTADOS_CUENTA = [
        ('activa', 'Activa'),
        ('suspendida', 'Suspendida'),
        ('cerrada', 'Cerrada'),
        ('bloqueada', 'Bloqueada')
    ]


    # Identificación 
    numero_cuenta = models.charField(max_length=20, unique=True)

    # Propietario
    titular = models.foreignKey(User, on_delete=models.PROTECT, related_name='cuentas')

    # Caracteristicas de la cuenta 
    tipo = models.charField(max_length=20, choices=TIPOS_CUENTA)
    estado = models.charField(max_length=20, choices=ESTADOS_CUENTA, default='activa')

    # Saldo - Crítico: Usar DecimalField para Precisión
    saldo_actual = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=Decimal('0.00'),
        help_text="Saldo actual de la cuenta en la moneda base"
    )

    # Límites y configuración
    limite_credito = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=Decimal('0.00')
    )

    # Metadatos temporales 
    fecha_apertura = models.DateTimeField(auto_now_add=True)
    fecha_ultima_actualizacion = models.DateTimeField(auto_now=True)

    # Configuracion adicional 
    permite_sobregiro = models.BooleanField(default=False)
    activa_para_transacciones = models.BooleanField(default=True)

    class Meta: 
        ordering = ['-fecha_apertura']
        verbose_name = 'Cuenta Bancaria'
        verbose_name_plural = 'Cuentas Bancarias'

    def __str__(self):
        return f"{self.numero_cuenta} - {self.titular.username} ({self.saldo_actual}$)"

    def saldo_disponible(self):
        if self.permite_sobregiro:
            return self.saldo_actual + self.limite_credito
        return max(self.saldo_actual, Decimal('0.00'))
