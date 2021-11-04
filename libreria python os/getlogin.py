import os

'''
os.getlogin() es una funcion de la libreria os
que devuelve el nombre del ususario activo en el
sistma
'''

usuario = os.getlogin()
print(usuario)
print( "tipo de dato: ", type(usuario))
