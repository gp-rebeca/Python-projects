#FUNCIÓN EXPONENCIAL
print(2**3) #lo mismo que hacer 2^3
#Vamos a hacer esto con un bucle for
def elevado_a(base,exponente):
    resultado=1
    for índice in range(exponente):
    #Vamos a repetir el bucle el número de veces al que esté elevada la base. Por ejemplo, si tienes 2 a la 3, se va a
    #repetir 3 veces.
        resultado=resultado* base #como está multiplicado por 1, en la segunda iteración ya tendrías la base
                                #multiplicada por sí misma, o sea la base a la 2
    return resultado

print(elevado_a(3,4))



