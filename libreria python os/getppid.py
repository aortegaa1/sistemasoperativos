import os

'''
 devuelve un dato de tipo entero que representa
 el ID del proceso actual en el sistema
'''
id_procesos = os.getppid()
print(id_procesos)
print( "tipo de dato: ", type(id_procesos))

os._exit(4)
print("algo")
