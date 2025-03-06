#Importamos las librerias necesarias

#Libreria para manejar los archivos JSON
import json
#Libreria para manejar las marcas de tiempo
from datetime import datetime
# Libreria pprint para mostrar mejor las tareas en la consola
import pprint

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
            print("Se guardo correctamente! \n")
    except:
        print("Error al crear el archivo JSON \n")
        
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
                id_tarea = max(tarea['No.'] for tarea in tareas) + 1  
            else:
                id_tarea = 1
                     
    # Maneja el error si no se encuentra el archivo    
    except FileNotFoundError as e:
        print(f"No se encontro el archivo. {e} \n")
    # Maneja el error si no logra leer el archivo    
    except json.JSONDecodeError as e:
        print(f"Error al leer el archivo JSON. {e} \n")
        
# crear las tareas    
def crear_tarea():
    '''
    recibe por consola: el nombre de la tarea, la tarea a realizar, 
    luego tiene menu para seleccionar la prioridad y el estado de la tarea
    y al final le pide al usuario en un formato especifico la fecha de finalizacion de la tarea
    '''
    
    try:
        global tareas    
        
        global id_tarea 
        
        nombre = input("Ingrese el nombre de la tarea a realizar: \n")
       
        tarea = input("Ingrese la tarea a realizar: \n")
       
        prioridades = ['baja', 'media', 'alta']
       
        seleccionP = int(input(f"Seleccione la prioridad de la tarea 1.{prioridades[0]} 2.{prioridades[1]} 3.{prioridades[2]}: \n"))
       
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
                print("Seleccione una opcion correcta! \n")
                           
        estados = ['pendiente', 'completado']
       
        seleccionE = int(input(f"Seleccione el estado de la tarea 1.{estados[0]} 2.{estados[1]}: \n" ))
       
        while True:    
            if seleccionE == 1:
                estado = estados[0]
                break
            elif seleccionE == 2:
                estado = estados[1]
                break
            else:
                print("Seleccione una opcion correcta! \n")
                crear_tarea() 
                           
        fecha_creacion = datetime.now().strftime("%d-%m-%Y, %H:%M")
        
        fecha_limite = input("Ingrese la fecha de finalizacion de la tarea (Separada por guiones(dia-mes-año)): \n")    
        
        nueva_tarea = {
            "No." : id_tarea,
            "Nombre" : nombre,
            "Fecha_Creacion": fecha_creacion,
            "Fecha_Limite": fecha_limite,
            "Tarea" : tarea,
            "Prioridad" : prioridad.lower(),
            "Estado": estado
            }
        
        tareas.append(nueva_tarea)   
        
        id_tarea += 1
        
        print("La tarea se añadio correctamente! \n")
        
    except Exception as e:
        print(f"La tarea no se pudo añadir {e} \n")
        guardar_tareas()
        
            
#buscar las tareas
def listar_tareas(): 
    '''
    Funcion para listar las tareas por 2 criterios o listar todas las tareas:
    criterio 1: listar por estado donde pide si es pendiente o completado
    criterio 2: listar por prioridad donde pide si es baja, media o alta
    
    '''
    # Desplegando menu de criterios de listar tareas
    menu = ['1. Listar por estado', '2. Listar por prioridad', '3. Listar todas']
    
    for item in menu:
        print(item)            
    seleccion = int(input("Seleccione la opcion deseada: \n"))
    
    # Opcion estado
    if seleccion == 1:
        select = int(input("Seleccione 1. Pendiente o 2. Completado: \n"))
        if select == 1:
            for item in tareas:
                if item['Estado']  == 'pendiente': 
                    print("Tareas pendientes: \n")
                    pprint.pprint(item , indent=4)
                    print()
        elif select == 2:
            for item in tareas:
                print("Tareas completadas: \n")
                if item['Estado'] == 'completado':
                    pprint.pprint(item , indent=4)
                    print()
        else:
            print("Seleccione la opcion correcta! \n")
            listar_tareas()

    # Opcion prioridad        
    elif seleccion == 2:
        select = int(input("Seleccione 1. baja, 2. media o 3. alta: \n"))
        if select == 1:
            for item in tareas:
                if item['Prioridad']  == 'baja':
                    print("Tareas con prioridad baja: \n") 
                    pprint.pprint(item , indent=4)
                    print()
        elif select == 2:
            for item in tareas:
                print("Tareas con prioridad media: \n")
                if item['Prioridad'] == 'media':
                    pprint.pprint(item, indent=4)
                    print()
        if select == 3:
            for item in tareas:
                print("Tareas con prioridad alta: \n")
                if item['Prioridad']  == 'alta': 
                    pprint.pprint(item, indent=4)
                    print()
        else:
            print("Seleccione una opcion valida! \n")
            listar_tareas()
    # Opcion todas
    elif seleccion == 3:
        for tarea in tareas:
            print("Todas las tareas: \n")
            pprint.pprint(tarea, indent=4)
            print()
    else:
        print("Seleccione una opcion valida! \n")
        listar_tareas()
    
# actualizar tareas
def actualizar_tarea():
    global tareas
    
    menu = ['No.', 'Nombre']
    for item in menu: 
        print(item)
    seleccion = int(input("Ingrese el tipo de busqueda de tarea 1. No. 2. Nombre: \n"))
    
    # Opcion numero de tarea o No.
    if seleccion == 1: 
        for tarea in tareas:
            print(tarea) 
            no_tarea = int(input("Ingrese el numero de la tarea: \n"))
            if tarea["No."] == no_tarea:
                actualizar(tarea)
                    
    elif seleccion == 2:
        for tarea in tareas:
            print(tarea)
            nombre_tarea = input("Ingrese el nombre de la tarea: \n")
            if tarea["Nombre"] == nombre_tarea:
                actualizar(tarea)
                
# Proceso de actualizacion separado                                             
def actualizar(item):
    # Menu para elegir lo que quieren editar de la tarea
    menu2 = ['1. Nombre',
             '2. Tarea',
             '3. Fecha Finalizacion',
             '4. Prioridad',
             '5. Estado']
    for i in menu2:
        print(i)
    seleccion2 = int(input("Seleccione una opcion: "))
    # Switch statement para machar la seleccion y realizar la accion deseada
    match seleccion2:
        case 1:
            nuevo_nombre = input("Ingrese el nuevo nombre de la tarea: \n")
            item.update({"Nombre": nuevo_nombre})   
        case 2:
            nueva_tarea = input("Ingrese la nueva tarea: \n")
            item.update({'Tarea': nueva_tarea})
        case 3:
            nueva_fecha = input("Ingrese la nueva fecha limite de la tarea: \n")
            item.update({'Fecha_Limite' : nueva_fecha})
        case 4:
            prioridades = ['1. baja', '2. media', '3. alta']
            for item in prioridades:
                print(item)
            nueva_prioridad = int(input("Seleccione la prioridad deseada: \n"))
            if nueva_prioridad == 1:
                item.update({'Prioridad': "baja"})
                print("Prioridad actualizada con exito! \n")        
            elif nueva_prioridad == 2:
                item.update({'Prioridad': "media"})
                print("Prioridad actualizada con exito! \n")
            elif nueva_prioridad == 3:
                item.update({'Prioridad': "alta"})
                print("Prioridad actualizada con exito! \n")    
            else:
                print("Ingrese una opcion correcta! \n")
        case 5:
            estados = ['1. pendiente', '2. completado']
            for item in estados:
                print(item)
            nuevo_estado = int(input("Seleccione el nuevo estado deseado: \n"))
            if nuevo_estado == 1:
                item.update({'Estado': "pendiente"})
                print("Estado actualizado con exito! \n")        
            elif nueva_prioridad == 2:
                item.update({'Estado': "completado"})
                print("Estado actualizado con exito! \n")    
            else:
                print("Ingrese una opcion valida! \n")                 
                   
def eliminar_tareas():
    '''
    funcion para eliminar las tareas con 2 criterios de busqueda: No. y Nombre
    Todo dentro de un menu para facilidad del usuario
    '''
    # Desplegamos menu corto de opciones
    menu = ['No.', 'Nombre' ]
    for item in menu: 
        print(item)
    seleccion = int(input("Ingrese el tipo de busqueda de tarea 1. No. 2. Nombre: \n"))
    
    # Opcion numero de tarea o No.
    if seleccion == 1: 
        for tarea in tareas: 
            no_tarea = int(input("Ingrese el numero de la tarea: \n"))
            if tarea['No.'] == no_tarea:
                tareas.remove(tarea)
            else:
                print("Ingrese un nombre de tarea valido! \n")
                eliminar_tareas()
                 
    # Opcion nombre de tarea              
    elif seleccion == 2: 
        for tarea in tareas:
            nombre_tarea = input("Ingrese el nombre de la tarea: \n")
            if tarea['Nombre'] == nombre_tarea:
                tareas.remove(tarea)
                print("Tarea eliminada exitosamente! \n")
            else:
                print("Ingrese un nombre de tarea valido! \n")
                eliminar_tareas()
    else: 
        print("Ingrese una opcion valida! \n")
        eliminar_tareas()