# API REST con FastAPI — Examen de Python (DAW)

API REST desarrollada con **FastAPI** como prueba del segundo trimestre de la asignatura
de Programación en Python, del ciclo de Desarrollo de Aplicaciones Web (DAW). Incluye
autenticación de usuarios, una capa de seguridad y persistencia en base de datos.

> Proyecto de aprendizaje. Lo mantengo público como muestra de mi trabajo con Python y
> el desarrollo de APIs back-end.

## Funcionalidades

- Endpoints REST construidos con **FastAPI**.
- **Autenticación** de usuarios (`auth.py`).
- **Seguridad**: hash de contraseñas y emisión/validación de tokens (`security.py`).
- Persistencia en **base de datos** (`db.py`, `models.py`).
- **Inyección de dependencias** de FastAPI (`deps.py`).
- Documentación interactiva automática (Swagger UI) disponible en `/docs`.

## Estructura del proyecto

| Archivo | Responsabilidad |
|---------|-----------------|
| `main.py` | Punto de entrada y definición de los endpoints de la API |
| `auth.py` | Lógica de autenticación (registro / inicio de sesión) |
| `security.py` | Hash de contraseñas y gestión de tokens |
| `db.py` | Conexión y sesión de base de datos |
| `models.py` | Modelos de datos |
| `deps.py` | Dependencias compartidas (inyección de dependencias) |

## Tecnologías

- Python 3
- FastAPI
- Uvicorn (servidor ASGI)

## Requisitos

- [Python 3](https://www.python.org/downloads/)

---

Autor: **Aitor Serrano** · [github.com/Aitorser](https://github.com/Aitorser)
