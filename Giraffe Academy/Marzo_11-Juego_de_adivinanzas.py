#JUEGO DE ADIVINANZAS
#Tenemos una palabra secreta y el usuario tiene que interactuar con el programa para adivinar la palabra.
palabra_secreta= "prado"
intento= " "
recuento_intentos= 0
limite_intentos= 3
intentos_agotados= False
while intento!= palabra_secreta and not(intentos_agotados):
    if recuento_intentos< limite_intentos:
        intento= input("Introduce una palabra: ")
        recuento_intentos +=1
    else:
        intentos_agotados= True

if intentos_agotados:
    print("No te quedan más intentos. Has perdido")
else:
    print("¡LO HAS ADIVINADO!")
