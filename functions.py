#Importamos las librerias necesarias
#Libreria para manejar los archivos JSON
import json
#Libreria para manejar las marcas de tiempo
from datetime import datetime, timedelta

'''
id_tarea (expresado como numero identificador de la tarea)
nombre (nombre asignado a la tarea a realizar)
fecha_creacion (fecha en que se crea la tarea con datetime)
fecha_limite (7 dias despues de la fecha de creacion)
tarea (un texto con la tarea a realizar detallado por el usuario)
prioridad(la prioridad de la tarea dividida en 3 categorias baja, media y alta)

'''
# Una lista con las tareas en diccionarios dentro de la lista
tareas = [{}]

# Una variable como contador para las tareas a realizar
id_tarea = 1 

# Funcion para guardar las tareas en un archivo JSON
def guardar_tareas(archivo='tareas.json'):
    try:
        with open(archivo, 'w') as file:
            json.dump(tareas, file, indent=4)
    except:
        print("Error al crear el archivo JSON ")
        
# Funcion para cargar las tareas desde el archivo JSON al comienzo del programa             
def cargar_tareas(archivo='tareas.json'):
    global id_tarea
    try:
        with open(archivo, 'r') as file:
            global tareas
            tareas = json.load(file) # Carga la lista desde el archivo json
            
            # Actualiza el contador basado en el ultimo contador de la lista
            if tareas:
                id_tarea = max(id_tarea['id'] for tarea in tareas) + 1
    # Maneja el error si no se encuentra el archivo    
    except FileNotFoundError as e:
        print(f"No se encontro el archivo. {e}")
    # Maneja el error si no logra leer el archivo    
    except json.JSONDecodeError as e:
        print(f"Error al leer el archivo JSON {e}")
        
# crear las tareas    
def crear_tarea(nombre, tarea, prioridad, estado):
    '''
    Ingresa 3 argumentos:
    Nombre: nombre para la tarea (hacerla facil de recordar)
    Tarea: Un texto descriptivo para tu tarea
    Prioridad: Una prioridad para tu tarea (baja, media o alta)    
    '''
    try:    
        global id_tarea 
        nombre = input("Ingrese el nombre de la tarea a realizar: ")
        tarea = input("Ingrese la tarea a realizar: ")
        prioridad = input("Ingrese la prioridad de la tarea (baja, media, alta): ")
        estado = input("Indique el estado de la tarea (pendiente o completada) : ")
        fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        fecha_limite = fecha_creacion + timedelta(days= 7)    
        nueva_tarea = {
            "No." : id_tarea,
            "Nombre" : nombre,
            "Fecha_Creacion": fecha_creacion,
            "Fecha_ Limite": fecha_limite,
            "Tarea" : tarea,
            "Prioridad" : prioridad,
            "Estado": estado
            }
        tareas.append(nueva_tarea)   
        id_tarea += 1
        print(f"La tarea se añadio correctamente! ")
        
    except Exception as e:
        print(f"La tarea no se pudo añadir {e}")
        
            
#buscar las tareas
def buscar_tareas(criterio):
    pass

# actualizar tareas
def actualizar_tarea(nombre_tarea, fecha_limite, prioridad, categoria):
    pass
