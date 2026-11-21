from pydantic import BaseModel
from typing import Optional


class VehiculoCreate(BaseModel):
    marca: str
    modelo: str
    anio: int
    categoria: Optional[str] = None
    precio_dia: float
    cantidad: int = 1


class VehiculoUpdate(BaseModel):
    marca: Optional[str] = None
    modelo: Optional[str] = None
    anio: Optional[int] = None
    categoria: Optional[str] = None
    precio_dia: Optional[float] = None
    cantidad: Optional[int] = None
    disponible: Optional[bool] = None


class VehiculoResponse(BaseModel):
    id: int
    marca: str
    modelo: str
    anio: int
    categoria: Optional[str] = None
    precio_dia: float
    cantidad: int
    disponible: bool