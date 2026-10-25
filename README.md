# Hackatón POO – Planta Atunera (Python)

Migración de la solución orientada a objetos del Grupo 2 (Hackatón POO), de Java a **Python 3.10+**.

**Autora:** Paulina Balladares

## Instalación

1. Instalar Python 3.10 o superior desde https://www.python.org/downloads/
2. Verificar la versión:

```bash
python --version
```

3. Clonar el repositorio:

```bash
git clone https://github.com/paulinaballadares797-bot/hackaton-poo-python.git
cd hackaton-poo-python
```

No requiere instalar librerías adicionales.

## Ejecución

```bash
python Main.py
```

Muestra dos casos válidos, dos casos inválidos (invariantes Fail-Fast) y el cierre del registro de fileteo.

## Archivos

- `operario_produccion.py`: clase `OperarioProduccion`
- `registro_fileteo.py`: clase `RegistroFileteo` con las invariantes de negocio
- `gestor_produccion.py`: clase `GestorProduccion`
- `Main.py`: flujo principal de demostración
