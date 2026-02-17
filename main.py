from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db import get_db
from models import Incidencia
from auth import router as auth_router
from deps import get_current_user

app = FastAPI(
    title="API Incidencias",
    description="Gestión de incidencias con Auth JWT",
    version="1.0.0",
)

app.include_router(auth_router)


class IncidenciaCreate(BaseModel):
    titulo: str
    descripcion: str
    prioridad: str
    estado: str


class IncidenciaResponse(IncidenciaCreate):
    id: int

    class Config:
        from_attributes = True


@app.get("/")
def root():
    return {"mensaje": "API de Incidencias funcionando. Ve a /docs"}


@app.get("/incidencias", response_model=list[IncidenciaResponse])
def listar_incidencias(db: Session = Depends(get_db)):
    return db.query(Incidencia).all()


@app.get("/users/me")
def read_users_me(usuario: str = Depends(get_current_user)):
    return {"usuario_autenticado": usuario}


@app.post("/incidencias", response_model=IncidenciaResponse, status_code=201)
def crear_incidencia(
    incidencia: IncidenciaCreate,
    db: Session = Depends(get_db),
    usuario: str = Depends(get_current_user),
):
    nueva = Incidencia(
        titulo=incidencia.titulo,
        descripcion=incidencia.descripcion,
        prioridad=incidencia.prioridad,
        estado=incidencia.estado,
    )
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva
