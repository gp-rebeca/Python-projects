#TRADUCTOR
#Idioma Suu
#vocales -> u
#-----------
#perro -> purru
#pupa -> pupu

def traduce(enunciado):
    traducción= ""
    for letra in (enunciado):
        if letra in "AEIOUaeiou": #si la letra es una vocal
            traducción= traducción + "u"
        elif letra in "ÁÉÍÓÚáéíóú":
            traducción= traducción + "ú"
        else:
            traducción= traducción + letra
    return traducción

print(traduce(input("Introduce una oración: ")))

#if letra.lower() in "aeiou":
#if letra.isupper():
    #traducción= traducción + "U"
#else:
    #traducción= traducción + "u"



