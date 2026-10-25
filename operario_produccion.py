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
    