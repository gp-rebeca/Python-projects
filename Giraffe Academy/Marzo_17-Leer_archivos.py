#LEER ARCHIVOS
#Para leer cositas de fuera de Python se usa el comando READ.
#Le das a File-open y presto.

texto_archivo= open("textopython.txt", "r")

#llamamiento, acción
#r-leer
#w-escribir
#r+w-leer y escribir

#Para ver si se lee bien
print(texto_archivo.readable()) #te devuelve true o false. Si le das a w en vez de a r, te va a salir false.
#print(texto_archivo.read()) #te escupe el texto

#print(texto_archivo.readline()) #te escupe la primera línea del texto

#print(texto_archivo.readline()) #te escupe la siguiente. Si lo vas repitiendo, te va leyendo línea a línea

#print(texto_archivo.readlines()) #te lo escupe tout juntito con forma de variable. Lo bueno es que ahora puedes acceder
                                #a la línea que quieras, especificando con un corchete
#print(texto_archivo.readlines()[3])

#También puedes hacer esto en un bucle
for clon in texto_archivo.readlines():
    print(clon)

texto_archivo.close()


