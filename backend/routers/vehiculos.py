from typing import Optional
from fastapi import APIRouter, HTTPException
from backend.database import obtener_conexion
from models.vehiculo import Vehiculo
from schemas.vehiculo_schema import VehiculoCreate, VehiculoUpdate, VehiculoResponse

router = APIRouter(prefix="/vehiculos", tags=["Vehículos"])


def buscar_fila(vehiculo_id: int):
    conexion = obtener_conexion()
    fila = conexion.execute("SELECT * FROM vehiculos WHERE id = ?", (vehiculo_id,)).fetchone()
    conexion.close()
    return fila


@router.get("/", response_model=list[VehiculoResponse])
def listar_vehiculos(marca: Optional[str] = None, anio: Optional[int] = None, 
                     solo_disponibles: bool = False):
    conexion = obtener_conexion()
    filas = conexion.execute("SELECT * FROM vehiculos").fetchall()
    conexion.close()

    # el map convierte cada fila de la BD en un objeto Vehiculo
    vehiculos = list(map(Vehiculo.desde_fila, filas))

    # filter y lambda son filtros opcionales por marca, año y disponibilidad
    if marca:
        vehiculos = list(filter(lambda v: v.marca.lower() == marca.lower(), vehiculos))
    if anio:
        vehiculos = list(filter(lambda v: v.anio == anio, vehiculos))
    if solo_disponibles:
        vehiculos = list(filter(lambda v: v.disponible, vehiculos))

    # el map convierte cada objeto en diccionario
    return list(map(lambda v: v.a_diccionario(), vehiculos))


@router.get("/{vehiculo_id}", response_model=VehiculoResponse)
def obtener_vehiculo(vehiculo_id: int):
    fila = buscar_fila(vehiculo_id)
    if fila is None:
        raise HTTPException(status_code=404, detail="Vehiculo no encontrado")
    return Vehiculo.desde_fila(fila).a_diccionario()


@router.post("/", response_model=VehiculoResponse, status_code=201)
def crear_vehiculo(vehiculo: VehiculoCreate):
    conexion = obtener_conexion()
    cursor = conexion.execute(
        "INSERT INTO vehiculos (marca, modelo, anio, categoria, precio_dia, cantidad) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        (vehiculo.marca, vehiculo.modelo, vehiculo.anio, vehiculo.categoria,
         vehiculo.precio_dia, vehiculo.cantidad),
    )
    conexion.commit()
    nuevo_id = cursor.lastrowid
    conexion.close()
    return Vehiculo.desde_fila(buscar_fila(nuevo_id)).a_diccionario()


@router.put("/{vehiculo_id}", response_model=VehiculoResponse)
def actualizar_vehiculo(vehiculo_id: int, cambios: VehiculoUpdate):
    if buscar_fila(vehiculo_id) is None:
        raise HTTPException(status_code=404, detail="Vehiculo no encontrado")

    # solo los campos que el cliente envio
    datos = cambios.model_dump(exclude_unset=True)
    if datos:
        columnas = ", ".join(f"{campo} = ?" for campo in datos)
        valores = list(datos.values()) + [vehiculo_id]
        conexion = obtener_conexion()
        conexion.execute(f"UPDATE vehiculos SET {columnas} WHERE id = ?", valores)
        conexion.commit()
        conexion.close()

    return Vehiculo.desde_fila(buscar_fila(vehiculo_id)).a_diccionario()


@router.delete("/{vehiculo_id}", status_code=204)
def eliminar_vehiculo(vehiculo_id: int):
    if buscar_fila(vehiculo_id) is None:
        raise HTTPException(status_code=404, detail="Vehiculo no encontrado")
    conexion = obtener_conexion()
    conexion.execute("DELETE FROM vehiculos WHERE id = ?", (vehiculo_id,))
    conexion.commit()
    conexion.close()