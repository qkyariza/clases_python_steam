from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

personas = {
    "1":{
        "Nombre":"Felipe",
        "Edad":23,
        "Ocupacion":"Ingeniero"
        },
    "2":{
        "Nombre":"David",
        "Edad":41,
        "Ocupacion":"Ingeniero"
        },
    "3":{
        "Nombre:":"Andres",
        "Edad":25,
        "Ocupacion":"Estudiante"
    }
}

@app.get("/")
def hello_worl_check():
    return {
        "titulo":"Biblioteca",
        "Version":"v0.0.0"
    }

@app.get("/personas")
def personas_all():
    return personas

class PersonaCreate(BaseModel):
    id:str
    nombre:str
    edad:int
    ocupacion:str

@app.post("/personas")
def personas_add(request:PersonaCreate):
    print(request)
    print(request.id)
    print(request.nombre)
    print(request.edad)
    personas[request.id] = {
        "Nombre":request.nombre,
        "Edad":request.edad,
        "Ocupacion":request.ocupacion
    }
    return request

@app.put("/personas")
def personas_modify(request:PersonaCreate):
    pass

@app.delete("/personas")
def personas_delete():
    pass

