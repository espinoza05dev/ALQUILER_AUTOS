from fastapi import FastAPI
from backend.database import crear_tablas, crear_admin_por_defecto
from routers import vehiculos, login

app = FastAPI(title="Rent a Car API")

crear_tablas()
crear_admin_por_defecto()
app.include_router(vehiculos.router)
app.include_router(login.router)

@app.get("/")
def inicio():
    return {"mensaje": "Hola mundo, la API de 'Rent a Car' esta funcionando"}