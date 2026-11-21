from models.persona import Persona


class Cliente(Persona):
    """Hereda de Persona y agrega los datos del cliente"""

    def __init__(self, id, nombre, identidad, telefono=None, direccion=None, usuario_id=None):
        super().__init__(id, nombre)
        self._identidad = identidad
        self._telefono = telefono
        self._direccion = direccion
        self._usuario_id = usuario_id

    def a_diccionario(self):
        datos = super().a_diccionario()
        datos.update({
            "identidad": self._identidad,
            "telefono": self._telefono,
            "direccion": self._direccion,
            "usuario_id": self._usuario_id,
        })
        return datos