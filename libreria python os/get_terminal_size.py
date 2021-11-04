import os

'''
funcion que devuelve un dato de tipo 'os.terminal_size'
que muestra el numero de lineas y columnas de la consola
'''
size_terminal = os.get_terminal_size()
print(size_terminal)
print( "tipo de dato: ", type(size_terminal))
