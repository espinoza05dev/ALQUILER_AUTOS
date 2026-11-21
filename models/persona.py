class Persona:
    """Clase padre, Cliente y Usuario heredan de ella"""

    def __init__(self, id, nombre):
        self._id = id          # son atributos protegidos por el guion
        self._nombre = nombre

    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or not valor.strip():
            raise ValueError(" 'nombre' no puede estar vacio")
        self._nombre = valor.strip()

    def a_diccionario(self):
        return {"id": self._id, "nombre": self._nombre}