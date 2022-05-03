#TRY/EXCEPT
#Vamos a aprender a detectar errores.

try:
    valor = 10 / 0
    número= int(input("Introduce un número: ")) #te lo convierte en entero (integer)
    print(número)
#except:
    #print("Input no válido")

#También te pone que 10/0 es un input no válido pero eso es mentiraaa. Pero es que el except se ejecuta cada vez qye hay
#un error en el código.
#Puedo dividir el except en dos
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Input no válido")
#Así especificas el error que tiene que "romper" el programa para que se ejecute el except.
#También puedes archivar los errores en variables (as nombre).



