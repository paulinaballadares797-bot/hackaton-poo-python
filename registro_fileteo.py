from datetime import datetime
from operario_produccion import OperarioProduccion

class RegistroFileteo:
    def __init__(self, fecha_produccion: datetime, lote: str, peso_inicial: float,
                 peso_lomos: float, peso_desperdicio: float, operario: OperarioProduccion):
        
       # Validación 1: conservación de masa (margen 0.001 por precisión de punto flotante)
        if abs((peso_lomos + peso_desperdicio) - peso_inicial) > 0.001:
            raise ValueError("Error de Invariante de Masa: peso_lomos + peso_desperdicio debe ser igual al peso_inicial.")

        # Validación 2: pesos no negativos e inicial mayor a cero
        if peso_inicial <= 0 or peso_lomos < 0 or peso_desperdicio < 0:
            raise ValueError("Los pesos no pueden ser negativos y el peso inicial debe ser mayor a cero.")


        self._fecha_produccion = fecha_produccion
        self._lote = lote
        self._peso_inicial = peso_inicial
        self._peso_lomos = peso_lomos
        self._peso_desperdicio = peso_desperdicio
        self._operario = operario

    def calcular_rendimiento_porcentaje(self) -> float:
        return (self._peso_lomos / self._peso_inicial) * 100.0

    def evaluar_rendimiento(self) -> str:
        rendimiento = self.calcular_rendimiento_porcentaje()
        if 45.0 <= rendimiento <= 51.0:
            return "Rendimiento Bueno"
        else:
            return "Rendimiento Malo"
