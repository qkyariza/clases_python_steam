from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

bibliteca = {}

@app.get("/")
def bibliteca_virtual():
    return("Bibloteca Steam V2")

@app.post("/agregar_usuario")
def agregar_usuario(
    id:int,
    nombre:str,
    libro:list
):
    diccionario_interno = {
        "Nombre":nombre,
        "Libro":libro
    }
    bibliteca[id] = diccionario_interno
    return bibliteca

@app.post("/agregar_libro")
def agregar_libro(
    id:int,
    libro:str
):
    bibliteca[id]["Libro"].append(libro)
    return bibliteca

@app.get("/leer_usuario")
def leer_usuario(
    id:int
):
    return bibliteca[id]

@app.get("/leer_todos_usuarrios")
def leer_todos_usuarios():
    return bibliteca

@app.put("/editar_libro")
def editar_libro(
    id:int,
    libro:str
):
    bibliteca[id]["Libro"] = libro
    return bibliteca

@app.delete("/borrar_usuario")
def eliminar_usuario(
    id:int
):
    del bibliteca[id]
    return bibliteca