#IF
#Vamos a crear una variable booleana.
es_fea= False
es_tonta= False

if es_fea:
    #lo que va aquí debajo indentado es lo que se ejecuta si la condición es verdadera
    print ("Eres fea")
else:
    #lo que se ejecuta si la condición es falsa
    print( "No eres fea")

if es_fea or es_tonta:
    #si se cumple UNA o LAS DOS
    print("Eres fea o tonta, o ambas")
else:
    print("No eres fea ni tonta. Suerte para ti.")

if es_fea and es_tonta:
    #si se cumplen LAS DOS
    print("Eres fea y tonta. Qué mal :(")
else:
    print("O no eres fea o no eres tonta o, afortunadamente, no eres ninguna de las dos.")

if es_fea and es_tonta:
    #si se cumplen LAS DOS
    print("Eres fea y tonta. Qué mal :(")
elif es_fea and not(es_tonta): #else if
    #and not niega lo que va entre paréntesis. Si es verdadero, lo hace falso y viceversa.
    print("Eres fea pero al menos no eres tonta")
elif not(es_fea) and es_tonta:  # else if
    # and not niega lo que va entre paréntesis. Si es verdadero, lo hace falso y viceversa.
    print("Eres tonta pero al menos no eres fea")
else:
    print("Afortunadamente, no eres ni fea ni tonta.")