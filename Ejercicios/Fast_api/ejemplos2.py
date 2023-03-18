
biblioteca = {
    "1":{
        "nombre":"felipe",
        "edad":"23",
        "libros":{
            "1":{
            "libro":"5am",
            "fecha":"13/3/2023",
            "estado":"prestado"
        },
            "2":{
            "libro":"100 años de soledad",
            "fecha":"13/5/2023",
            "estado":"prestado"
        },
        }
    },
    "2":{
        "nombre":"Sharid",
        "edad":"23",
        "libros":{
            "1":{
            "libro":"habtios atomicos",
            "fecha":"13/3/2023",
            "estado":"prestado"
        },
            "2":{
            "libro":"poesia y mitos",
            "fecha":"13/5/2023",
            "estado":"prestado"
        },
        }
    }
}


@app.get("/{id}")
def hola(id:str):
    return biblioteca[id]

@app.get("/libro/{id}/{id2}")
def hola(id:str,id2:str):
    return biblioteca[id]["libros"][id2]  