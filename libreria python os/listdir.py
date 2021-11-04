import os

'''
 devualve una lsita de cadenas de texto con los nombres
 de los archivos ubicados en la ruta suministrade
'''
directorios = os.listdir("C:\\")
print(directorios)
print( "tipo de dato: ", type(directorios))
print( "tipo de dato: ", type(directorios[0]))
