
nombre_archivo = "tareas.txt"

class Tareas:
    try: 
        def NuevaTarea(self, tarea):
            with open("tareas.txt" , "a") as archivo: # append 
                archivo.write(tarea + "\n")
    except Exception as e:
            print(f"Error al agregar la tarea: {e}")
    
    def MostrarTareas(self):
        with open("tareas.txt", "r") as archivo:
            print("************************")
            print(archivo.read())
            print("************************")     

    def EliminarTarea(self, tarea):
        with open("tareas.txt" , "r") as archivo:
            lineas = archivo.readlines()
        
        # Almacenar en la variable todas las tareas excepto la que voy a eliminar
        lineas = [linea for linea in lineas if linea.strip() != tarea]

        with open("tareas.txt", "w") as archivo:
            archivo.writelines(lineas)

n = Tareas()

while(True):
    print("Gestion de tareas")
    print("\n1. Agregar una nueva tarea ")
    print("2. Mostrar todas las tareas guardadas")
    print("3. Mostrar tarea como terminada")
    print("4. Salir")

    op = int(input(">>"))

    if (op == 1):   
        tarea = input("Ingresa la tarea: ")
        n.NuevaTarea(tarea)
    elif (op == 2):
        n.MostrarTareas()
    elif (op == 3): # Marcar una tarea como completada (eliminarla del archivo)
        tarea = input("Ingresa la tarea finalizada: ")
        n.EliminarTarea(tarea)
    elif (op == 4):
        break
        










# Taller
# Gestión de una Lista de Tareas con POO
# Descripción del Ejercicio
# Vas a crear una aplicación simple que gestione una lista de tareas (To-Do List) utilizando clases y objetos . La lista de tareas se
# almacenará en un archivo de texto llamado tareas.txt. El programa permitirá:
# Agregar una nueva tarea al archivo.1.
# Mostrar todas las tareas guardadas en el archivo.2.
# .3.
# Este ejercicio combina:
# POO : Crearás una clase para gestionar las tareas.
# Manipulación de archivos : Leerás y escribirás en un archivo de texto.
# Manejo de excepciones : Capturarás errores comunes como archivos inexistentes.