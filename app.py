'''
Proyecto final del curso Curso de Fundamentos de Programación con Python

Grupo conformado por:

Oriver Segura
Mario Melvin Cabrera Martinez

'''
    
# Importamos las librerias necesarias
# Libreria Time para poner un sleep a la salida y no sea brusca
import time
# Libreria con las funciones logicas de la app
from functions import *

tareas

cargar_tareas()
def main():
    # Bucle while para el funcionamiento continuo de la app
    while True:
        # Mensaje de bienvenida a la app y el menu de opciones
        print("****** Bienvenid@ a la App de Gestion de Tareas ***** \n")
        time.sleep(0.5)
        print("Menu: \n")
        time.sleep(0.5)
        # Lista con el menu de opciones
        menu = ["1. Crear Tarea",
                "2. Listar Tareas",
                "3. Actualizar Tareas",
                "4. Eliminar Tareas",
                "5. Salir"]
        # Mostramos el menu al usuario con un bucle for
        for item in menu:
            time.sleep(0.5)
            print(item)
        # Captamos la seleccion del usuario    
        seleccion = int(input("Seleccione una opcion: \n"))
        
        # Usamos match para proceder con las decisiones del usuario    
        match seleccion:
            case 1:
                crear_tarea()
            case 2:
                listar_tareas()
            case 3:
                actualizar_tarea()
            case 4:
                eliminar_tareas()
            case 5:
                print("Saliendo de la app...... \n")
                guardar_tareas()
                # Tiempo de espera al usuario por decision del desarrollador
                time.sleep(5)
                break
            case _:
                print("Seleccione una opcion valida! \n")


if __name__ == "__main__":
    main()