from models.persona import Persona


class Usuario(Persona):
    """Hereda de Persona y agrega correo, clave y rol"""

    def __init__(self, id, nombre, correo, clave, rol="cliente"):
        super().__init__(id, nombre) # llama al constructor del padre
        self._correo = correo
        self._clave = clave
        self._rol = rol

    @property
    def correo(self):
        return self._correo

    @property
    def rol(self):
        return self._rol

    def verificar_clave(self, clave):
        return self._clave == clave

    def es_admin(self):
        return self._rol == "admin"

    def a_diccionario(self):
        datos = super().a_diccionario() # reutiliza lo del padre
        datos["correo"] = self._correo
        datos["rol"] = self._rol # la clave no se devuelve
        return datos