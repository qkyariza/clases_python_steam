diccionario = {"Nombre":"Felipe"}

diccionario["Apellido"] = "Gonzalez"
temp = {"Edad":23,
        "Sexo":"M",
        "Nombre":"Gabriela",
        "Profesion":"INg.Sistema"
        }

#diccionario["Extra"] = temp #diccionario anidado
# diccionario.update(temp) #diccionario concatenado
diccionario.pop("Sexo")
diccionario["Extra"].pop("Sexo")
diccionario["Extra"]["Profesion"] = ["Profesor","ing","Bailarin","Modelo","Batman"]
diccionario["Extra"]["Profesion"].append("Astronauta")