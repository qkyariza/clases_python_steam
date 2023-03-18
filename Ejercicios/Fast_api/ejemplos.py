@app.get("/saludo")
def Hola():
    return("Hola mundo desde FASTAPI")


@app.get("/saludo/david")
def Hola():
    return("Hola David")


@app.get("/saludo/miguel")
def Hola():
    return("Hola Miguel")


@app.get("/hola/{nombre}")
def hola(nombre):
    return f"hola {nombre}"


@app.get("/adios")
def Adios():
    return("Adios mundo cruel")


@app.get('/estado')
def Como_estas():
    return("Como estas?")


@app.get('/edad')
def Edad():
    return("Cuantos anos tienes?")


@app.get("/direccion")
def Direccion():
    return("Cual es tu correo electtonico?")

@app.get("/hola/{nombre}/{edad}")
def hola(nombre:str,edad:int):
    return f'la edad de {nombre} es {edad} anos'

@app.get('/area_cuadrado/{lado_a}/{lado_b}')
def area_cuadrado(lado_a:float,lado_b:float):
    return lado_a*lado_b

@app.get("/mayor_edad/{edad}")
def mayor_edad(edad:int):
    if edad > 18:
        return f"Eres mayor de edad"
    else:
        return f"Eres menor de edad"