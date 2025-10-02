import csv 
import json
from pathlib import Path
from datetime import datetime

class ProcesadorDatosError(Exception):
    pass

class ProcesadorDatos:
    def __init__(self, directorioTrabajo="datos_procesados"):
        self.directorio = Path(directorioTrabajo)
        self.directorio.mkdir(exist_ok=True)
        self.log_file = self.directorio / "procesamiento.log"

    def log(self, mensaje):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {mensaje}\n")
            print(f"[{timestamp}] {mensaje}")

    def procesarCSV(self, archivoEntrada):
        try:
            archivoPath = Path(archivoEntrada)
            if not archivoPath.exists():
                raise FileNotFoundError(f"Archivo {archivoEntrada} no encontrado")
            self.log(f"Iniciando procesamiento de {archivoEntrada}")

            datos = []
            with open(archivoPath, "r", encoding="utf-8") as f:
                lector = csv.DictReader(f)
                for row in lector:
                    datos.append(row)

            self.log(f"Leídas {len(datos)} filas")

            datosProcesados = []
            for fila in datos:
                try:
                    filaProcesada = fila.copy()
                    if "edad" in fila:
                        filaProcesada["edad"] = float(fila["edad"])
                    if "salario" in fila:
                        filaProcesada["salario"] = float(fila["salario"])
                    datosProcesados.append(filaProcesada)
                except ValueError as e:
                    self.log(f"Error procesando fila {fila}: {e}")
                    continue
            archivoSalida = self.directorio / f"procesado_{archivoPath.stem}.json"
            with open(archivoSalida, "w", encoding="utf-8") as f:
                json.dump(datosProcesados, f, indent=2, ensure_ascii=False)
            self.log(f"Datos Guardados en {archivoSalida}")
            return datosProcesados
        except Exception as e:
            self.log(f"Error crítico: {e}")
            raise ProcesadorDatosError(f"Fallo en procesamiento: {e}")

# Crear datos de prueba
datosPrueba = """nombre,edad,salario
Jesus Moreno,28,100000
Carlos,35,90000
Juan,27,1000000"""

with open("empleados_prueba.csv", "w") as f:
    f.write(datosPrueba)

# Usar procesador 
procesador = ProcesadorDatos()
try:
    result = procesador.procesarCSV("empleados_prueba.csv")
    print(f"\nProcesamiento completado. {len(result)} registros procesados")
except ProcesadorDatosError as e:
    print(f"Error en procesamiento: {e}")
