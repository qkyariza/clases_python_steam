Ejercicio de bibliotecario:

### Contexto de la tarea
Trabajas en una biblioteca y tienes el trabajo de registrar los usuairos que prestan libros, para eso realizas una script en python donde guardas en un diccionario el nombre del usuario y el nombre del libro de presto, ejemplo ````{"felipe": "habitos atomicos"}````, para que funcione correctamente creas un CRUD (Create, Read, Update y Delete) con las siguientes funciones ````agregar_usuario, eliminar_usuario, actualizar_usuario, visualiazr_usuario`````
### Requisitos de la Tarea:
- las funciones deben tener buenas practicas con Python.
- El codigo debe cumplir con el principio de Single Responsability, cada archivo de python deben tener un función.
- La tarea debe estar montada en GitHub.
- El archivo principal debe contar con ````__name__=="__main__"````

### Anotaciones.
En el siguiente enlace se cuenta con un **````EJEMPLO INCOMPLETO````** de como deberia ser el programa y el ejemplo está en **````LISTAS````**, los estudiantes deben hacerlo con diccionarios.

Modificacion de la tarea #1
Ademas del nombre de la persona, pueda guardar un diccionario de los libros que presto y la fecha.

{"felipe":[
    
    {"libro":"habitos atomicos",
    "fecha":"2023-02-14"},
    
    {"libro":"Club 5 am",
    "fecha":"2023-02-15"},
    
    {"libro":"python completo",
    "fecha":"2023-03-05"},
]}

# modificar # 2
# eliminar usuario (con validiación). eliminar libro

# modificar  # 3
# si el libro está prestado o devuelto. validar estado de un libro

{"felipe":[
    
    {"libro":"habitos atomicos",
    "fecha":"2023-02-14",
    "estado":"prestado"},
    
    {"libro":"Club 5 am",
    "fecha":"2023-02-14",
    "estado":"devuelto"},
]}