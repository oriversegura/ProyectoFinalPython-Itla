#Importamos las librerias necesarias

#Libreria para manejar los archivos JSON
import json
#Libreria para manejar las marcas de tiempo
from datetime import datetime

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
            print("Se guardo correctamente!")
    except:
        print("Error al crear el archivo JSON ")
        
# Funcion para cargar las tareas desde el archivo JSON al comienzo del programa             
def cargar_tareas(archivo='tareas.json'):
    global id_tarea
    try:
        with open(archivo, 'r') as file:
            global tareas
            tareas = json.load(file) # Carga la lista desde el archivo json
            print("Se cargo correctamente!")
            # Actualiza el contador basado en el ultimo contador de la lista
            if tareas:
                id_tarea = max(tarea['No.' ] for tarea in tareas) + 1  
            else:
                tareas = 1
                
                
    # Maneja el error si no se encuentra el archivo    
    except FileNotFoundError as e:
        print(f"No se encontro el archivo. {e}")
    # Maneja el error si no logra leer el archivo    
    except json.JSONDecodeError as e:
        print(f"Error al leer el archivo JSON. {e}")
        
# crear las tareas    
def crear_tarea():
    '''
    Ingresa 3 argumentos:
    Nombre: nombre para la tarea (hacerla facil de recordar)
    Tarea: Un texto descriptivo para tu tarea
    Prioridad: Una prioridad para tu tarea (baja, media o alta)    
    '''
    
    try:
        global tareas    
        global id_tarea 
        nombre = input("Ingrese el nombre de la tarea a realizar: ")
        tarea = input("Ingrese la tarea a realizar: ")
        prioridades = ['baja', 'media', 'alta']
        seleccionP = int(input(f"Seleccione la prioridad de la tarea 1.{prioridades[0]} 2.{prioridades[1]} 3.{prioridades[2]}: "))
        while True:    
            if seleccionP == 1:
                prioridad = prioridades[0]
                break
            elif seleccionP == 2:
                prioridad = prioridades[1]
                break
            elif seleccionP == 3:
                prioridad = prioridades[2]
                break
            else:
                print("Seleccione una opcion correcta!")  
        estados = ['pendiente', 'completado']
        seleccionE = int(input(f"Seleccione el estado de la tarea 1.{estados[0]} 2.{estados[1]} :" ))
        while True:    
            if seleccionE == 1:
                estado = estados[0]
                break
            elif seleccionE == 2:
                estado = estados[1]
                break
            else:
                print("Seleccione una opcion correcta!")            
        fecha_creacion = datetime.now().strftime("%d-%m-%Y, %H:%M")
        fecha_limite = input("Ingrese la fecha de finalizacion de la tarea (Separada por guiones): ")    
        nueva_tarea = {
            "No." : id_tarea,
            "Nombre" : nombre,
            "Fecha_Creacion": fecha_creacion,
            "Fecha_ Limite": fecha_limite,
            "Tarea" : tarea,
            "Prioridad" : prioridad.lower(),
            "Estado": estado
            }
        tareas.append(nueva_tarea)   
        id_tarea += 1
        print(f"La tarea se añadio correctamente! ")
        
    except Exception as e:
        print(f"La tarea no se pudo añadir {e}")
        guardar_tareas()
        
            
#buscar las tareas
def listar_tareas(): 
    pass

# actualizar tareas
def actualizar_tarea():
    pass

def eliminar_tareas():
    pass