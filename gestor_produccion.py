from registro_fileteo import RegistroFileteo 

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
