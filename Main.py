from datetime import datetime
from operario_produccion import OperarioProduccion
from registro_fileteo import RegistroFileteo
from gestor_produccion import GestorProduccion


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
