from pydantic import BaseModel


class LoginRequest(BaseModel):
    correo: str
    clave: str


class LoginResponse(BaseModel):
    id: int
    nombre: str
    correo: str
    rol: str
    mensaje: str