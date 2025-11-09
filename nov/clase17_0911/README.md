### Qué es un ORM ???

Un ORM (Object-Relational Mapper) es una técnica de programación que permite mapear objetos de programación orientada a objetos con tablas de bases de datos relacionales.

**Ventajas del ORM en sistemas financieros:**

- **Precisón decimal**: Django maneja automaticamente la precisón requerida para cálculos monetarios
- **Integridad transaccional**: Garantiza que las operaciones financieras sean atómicas
- **Auditoria autómatica:** Facilita el seguimiento de cambios de datos críticos
- **Validación de datos:** Previene errores comunes en cálculos financieros

### Arquitectura de Datos Financieros

En un sistema de inteligencia financiera, los datos se organizan en capas jerárquicas:

```
Capa de Análisis
|-- Reportes y KPIs
|-- Alertas autómaticas
|-- Métricas de rendimiento

Capa de transacciones
|-- Movimientos de dinero
|-- Transferencias
|-- Pagos y cobros

Capa de entidades
|-- Cuentas bancarias
|-- Clientes/Usuarios
|-- Instituciones dinancieras

Capa de Configuración
|-- Tipos de cuenta
|-- Categorías de gastos
|-- Parámetros del sistema
```

**1. Precisión Decimal Absoluta**

# ❌NUNCA usar FloatField()

precio = models.FloatField() # Puede causar errores de redondeo

# SIEMPRE usar DecimalField para dinero

precio = models.DecimalField(max_digits=15, decimal_places=2)

**2. Inmutabilidad de Transacciones**

```python
# Las transacciones financieras NUNCA se modifican, solo se crean nuevas
class Transaccion(models.Model):
  fecha_creacion = models.DateTimeField(auto_now_add=True)
  # Nunca incluir auto_now=True en Transacciones
```

**3. Trazabilidad Completa**

```python
# Cada operación debe ser rastreable
class MovimientoFinanciero(models.Model):}
  usuario_creacion = models.ForeignKey(User, on_delete=models.PROTECT)
  fecha_operacion = models.DateTimeField()
  referencia_externa = models.CharField(max_length=100, unique=True)
```

### Modelado de Cuentas Bancarias

Una cuenta bancaria en un sistema financiero debe capturar:

- **Identificación única**: Número de cuenta
- **Saldo actual**: con Precisión decimal Absoluta
- **Metadatos**: Tipo, estado, fecha de apertura/cierre
- **Relacionales**: Propitario, banco, sucursal
