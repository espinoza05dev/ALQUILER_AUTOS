#Sistema de Alquiler de Autos

## 📁 Estructura del proyecto

```
rent_a_car/
│
├── README.md
├── .gitignore
│
├── backend/                        # Python + FastAPI
│   ├── venv/                       # entorno virtual (no se sube a git)
│   ├── requirements.txt            # dependencias del proyecto
│   └── app/
│       ├── main.py                 # punto de entrada, crea la app FastAPI, routers y CORS
│       ├── database.py             # conexión a la base de datos
│       │
│       ├── models/                 # clases POO (entidades)
│       │   ├── usuario.py
│       │   ├── cliente.py
│       │   ├── vehiculo.py
│       │   ├── reserva.py
│       │   ├── alquiler.py
│       │   ├── devolucion.py
│       │   ├── mantenimiento.py
│       │   ├── pago.py
│       │   └── factura.py
│       │
│       ├── schemas/                # modelos Pydantic (validación de datos)
│       │   ├── login_schema.py
│       │   ├── usuario_schema.py
│       │   ├── cliente_schema.py
│       │   ├── vehiculo_schema.py
│       │   ├── reserva_schema.py
│       │   ├── alquiler_schema.py
│       │   ├── devolucion_schema.py
│       │   ├── mantenimiento_schema.py
│       │   ├── pago_schema.py
│       │   └── factura_schema.py
│       │
│       ├── routers/                # endpoints por recurso
│       │   ├── login.py            # /login
│       │   ├── usuarios.py         # /usuarios
│       │   ├── clientes.py         # /clientes
│       │   ├── vehiculos.py        # /vehiculos
│       │   ├── reservas.py         # /reservas
│       │   ├── alquileres.py       # /alquileres
│       │   ├── devoluciones.py     # /devoluciones
│       │   ├── mantenimientos.py   # /mantenimientos
│       │   ├── pagos.py            # /pagos
│       │   └── facturas.py         # /facturas
│       │
│       └── services/               # lógica de negocio
│           ├── auth_service.py             # validación de login
│           ├── disponibilidad_service.py   # disponibilidad de vehículos
│           ├── costo_service.py            # cálculo de costo total
│           └── factura_service.py          # generación de facturas y contratos
│
├── admin_portal/                   # HTML + PHP + Bootstrap
│   ├── index.php                   # login del administrador
│   ├── dashboard.php
│   ├── config/
│   │   └── api.php                 # URL base de la API y función para consumirla
│   ├── includes/                   # header, footer y navbar reutilizables
│   ├── pages/
│   │   ├── usuarios.php
│   │   ├── clientes.php
│   │   ├── vehiculos.php
│   │   ├── reservas.php
│   │   ├── mantenimientos.php
│   │   ├── devoluciones.php
│   │   ├── alquileres.php
│   │   └── facturas.php
│   └── assets/
│       ├── css/
│       ├── js/
│       └── img/
│
└── user_portal/                    # JavaScript + HTML5 + CSS3
    ├── index.html                  # inicio / login
    ├── registro.html
    ├── vehiculos.html              # lista y filtros por categoría
    ├── detalle_vehiculo.html
    ├── reservar.html
    ├── mis_reservas.html
    ├── historial.html
    ├── css/
    │   └── styles.css
    ├── js/
    │   ├── api.js                  # peticiones fetch() al backend
    │   ├── auth.js                 # login y registro
    │   ├── vehiculos.js
    │   └── reservas.js
    └── img/
```
