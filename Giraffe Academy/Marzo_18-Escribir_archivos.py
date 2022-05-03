#ESCRIBIR EN ARCHIVOS

#Quiero añadir un clon a la lista
textito= open("textopython.txt", "a")
#a-append

textito.write("Krystal-Youtuber")
#Ojo, que si lo corres muchas veces te lo va añadiendo al lado y la lías. Y ES PERMANENTE.

textito.write("\nSarah-Punk") #línea nueva \n

#También puedes sobreescribir, poniendo w en vez de a. Te lo borra todito y te pone algo nuevo.


textito.close()
