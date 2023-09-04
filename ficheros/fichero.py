from io import open
import pathlib
import shutil

#abrir un archivo
ruta = str(pathlib.Path().absolute()) + "/nombre_archivo.txt"
archivo = open(ruta,"+a")

#escribir en el archivo
archivo.write("Agregando una linea de texto al archivo \n")

#cerrar archivo
archivo.close()

#abrir un archivo con permiso de lectura r
ruta = str(pathlib.Path().absolute()) + "/nombre_archivo.txt"
archivo_leer = open(ruta,"r")

"""
#leer contenido
contenido = archivo_leer.read()
print(contenido)
"""

#leer contenido y guardar en una lista
lista = archivo_leer.readlines()
archivo_leer.close()

"""
for linea in lista:
    print("- "+ linea)
"""

#copiar un archivo Nota: import shutil
#ruta_original = str(pathlib.Path().absolute()) + "/nombre_archivo.txt"
#ruta_nueva = str(pathlib.Path().absolute()) + "/nombre_archivo_copiado.txt"
#shutil.copyfile(ruta_original,ruta_nueva)
#ruta_alternativa = str(pathlib.Path().absolute()) + "/../practice_udemy/ficheros/archivo_copiado.txt"
#shutil.copyfile(ruta_original, ruta_alternativa) 

"""
#mover
ruta_original = str(pathlib.Path().absolute()) + "/nombre_archivo_copiado.txt"
ruta_nueva = str(pathlib().absolute()) + "/nombre_archivo_copiado.txt"

shutil.move(ruta_original, ruta_nueva)
"""

