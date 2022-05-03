#FUNCIONES
#Colección de código que cumple una tarea específica. Para hacer la tarea, llamas a la función.
#Vamos a crear una función que salude al usuario. Para ello, empezamos definiendo la función con "def" y le ponemos
#un nombre, sin paréntesis ni comillas ni nada. A continuación del nombre, pones paréntesis y dos puntos.
#Cada vez que pulso enter, se indenta lo siguiente. Lo que va dentro del código de la función tiene que estar indentado.

def dihola():
    print("Hola, usuario/a")

#Para ejecutar la función, tengo que llamarla
dihola()

#Ahora vamos a darle un poco de info a la función. La información que le das a una función se llama PARÁMETRO.
#Vamos a decirle cómo se llama el usuario al que tiene que saludar (lo defino como nueva función para que me quede
#separado de lo de arriba).
def di_hola(nombre):
    print("Hola, " + nombre)

di_hola("Rebeca")
di_hola("caracola")

#Puedes definir tantos parámetros como quieras.

def bienvenida(nombre, edad):
    print("Hola, " + nombre + ", tienes " + edad + " años.")

bienvenida("Rebeca","22")

#Para meter parámetros numéricos sin necesidad de usar comillas, tienes que definirlos como string.

def bienvenida2(nombre, edad):
    print("Hola, " + nombre + ", tienes " + str(edad) + " años.")

bienvenida2("Luisa", 288)
