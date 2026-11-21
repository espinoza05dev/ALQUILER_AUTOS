class Vehiculo:
    def __init__(self, id, marca, modelo, anio, categoria, precio_dia, cantidad, disponible):
        self._id = id
        self._marca = marca
        self._modelo = modelo
        self._anio = anio
        self._categoria = categoria
        self._precio_dia = precio_dia
        self._cantidad = cantidad
        self._disponible = bool(disponible)

    @property
    def marca(self):
        return self._marca

    @property
    def anio(self):
        return self._anio

    @property
    def disponible(self):
        # Se puede alquilar solo si esta disponible y si hay unidades en el inventario
        return self._disponible and self._cantidad > 0

    @classmethod
    def desde_fila(cls, fila):
        """Convierte una fila de la base de datos en un objeto Vehiculo."""
        return cls(fila["id"], fila["marca"], fila["modelo"], fila["anio"],
                   fila["categoria"], fila["precio_dia"], fila["cantidad"],
                   fila["disponible"])

    def a_diccionario(self):
        return {
            "id": self._id,
            "marca": self._marca,
            "modelo": self._modelo,
            "anio": self._anio,
            "categoria": self._categoria,
            "precio_dia": self._precio_dia,
            "cantidad": self._cantidad,
            "disponible": self.disponible,
        }





    