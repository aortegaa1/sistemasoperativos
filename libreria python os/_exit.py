import os

'''
 salida del proceso actual

 en el ejemplo el programa las instrucciones se ejecutan de manera
 secuencial, cuando se llama la funcion os._exit el programa deje de
 ejecutarse (se cierra el proceso)
'''
print("primera instruccion del programa")
print("segunda instruccion del programa")
# se suspende la ejecucion con codigo de retorno 5
os._exit(4)
# las sentencias dede aqui no se ejecutaran
print("trecera instruccion del programa")
print("cuarta instruccion del programa")
