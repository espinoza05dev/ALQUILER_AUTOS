from fastapi import APIRouter, HTTPException
from backend.database import obtener_conexion
from models.usuario import Usuario
from schemas.login_schema import LoginRequest, LoginResponse

router = APIRouter(tags=["Login"])


@router.post("/login", response_model=LoginResponse)
def login(datos: LoginRequest):
    conexion = obtener_conexion()
    fila = conexion.execute(
        "SELECT * FROM usuarios WHERE correo = ?", (datos.correo,)
    ).fetchone()
    conexion.close()

    # es el mismo mensaje si falla el correo o la clave
    error = HTTPException(status_code=401, detail="Correo o clave incorrectos")

    if fila is None:
        raise error

    # se crea un objeto Usuario con los datos de la fila
    usuario = Usuario(fila["id"], fila["nombre"], fila["correo"],
                      fila["clave"], fila["rol"])

    if not usuario.verificar_clave(datos.clave):
        raise error

    respuesta = usuario.a_diccionario()   # no incluye la clave
    respuesta["mensaje"] = "Inicio de sesion exitoso"
    return respuesta