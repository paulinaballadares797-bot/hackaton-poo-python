from datetime import datetime

# ==========================================
# 1. CLASE: OperarioProduccion
# ==========================================
class OperarioProduccion:
    def __init__(self, codigo: str, nombre: str, turno: str):
        self._codigo = codigo
        self._nombre = nombre
        self._turno = turno

    def obtener_codigo(self) -> str:
        return self._codigo

    def obtener_nombre(self) -> str:
        return self._nombre

    def obtener_turno(self) -> str:
        return self._turno


# ==========================================
# 2. CLASE: RegistroFileteo
# ==========================================
class RegistroFileteo:
    def __init__(self, fecha_produccion: datetime, lote: str, peso_inicial: float,
                 peso_lomos: float, peso_desperdicio: float, operario: OperarioProduccion):
        
        # 1. Invariante: pesos no negativos e inicial mayor a cero
        if peso_inicial <= 0 or peso_lomos < 0 or peso_desperdicio < 0:
            raise ValueError("Los pesos no pueden ser negativos y el peso inicial debe ser mayor a cero.")

        # 2. Invariante: conservación de masa (margen 0.001 por precisión de punto flotante)
        if abs((peso_lomos + peso_desperdicio) - peso_inicial) > 0.001:
            raise ValueError("Error de Invariante de Masa: pesoLomos + pesoDesperdicio debe ser igual al pesoInicial.")

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


# ==========================================
# 3. CLASE: GestorProduccion
# ==========================================
class GestorProduccion:
    def __init__(self):
        self._registros = []

    def agregar_registro(self, registro: RegistroFileteo):
        self._registros.append(registro)

    def cerrar_registro_fileteo(self):
        buenos = 0
        malos = 0

        for reg in self._registros:
            evaluacion = reg.evaluar_rendimiento()
            if evaluacion == "Rendimiento Bueno":
                buenos += 1
            else:
                malos += 1

        print("=== CIERRE DE REGISTRO DE FILETEO ===")
        print(f"Total de registros evaluados: {len(self._registros)}")
        print(f"Productos con Rendimiento Bueno: {buenos}")
        print(f"Productos con Rendimiento Malo: {malos}")


# ==========================================
# 4. FLUJO PRINCIPAL
# ==========================================
if __name__ == "__main__":
    operario = OperarioProduccion("OP-001", "Carlos Mendoza", "Mañana")
    gestor = GestorProduccion()

    print("--- CASO VÁLIDO 1: rendimiento bueno (48%) ---")
    try:
        r1 = RegistroFileteo(datetime.now(), "LOTE-001", 100.0, 48.0, 52.0, operario)
        gestor.agregar_registro(r1)
        print("Registro creado:", r1.evaluar_rendimiento())
    except ValueError as e:
        print("Error:", e)

    print("\n--- CASO VÁLIDO 2: rendimiento malo (40%) ---")
    try:
        r2 = RegistroFileteo(datetime.now(), "LOTE-002", 100.0, 40.0, 60.0, operario)
        gestor.agregar_registro(r2)
        print("Registro creado:", r2.evaluar_rendimiento())
    except ValueError as e:
        print("Error:", e)

    print("\n--- CASO INVÁLIDO 1: la masa no se conserva ---")
    try:
        RegistroFileteo(datetime.now(), "LOTE-003", 100.0, 60.0, 30.0, operario)
    except ValueError as e:
        print("Error capturado:", e)

    print("\n--- CASO INVÁLIDO 2: peso negativo ---")
    try:
        RegistroFileteo(datetime.now(), "LOTE-004", 100.0, -10.0, 110.0, operario)
    except ValueError as e:
        print("Error capturado:", e)

    print()
    gestor.cerrar_registro_fileteo()