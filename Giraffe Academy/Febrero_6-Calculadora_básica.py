#CONSTRUYENDO UNA CALCULADORA BÁSICA
num1= input("Introduce el primer número: ")
num2= input("Introduce el segundo número: ")
suma= num1 + num2 #¡OJO, CUIDAO'! Esto lo que hace es interpretar los números como palabras y ponerlos a continuación
print(suma)
#Tenemos que convertir esas varaibles en números para que el programa nos entienda. Esto se puede hacer con dos
#funciones de Python: int (integer, números enteros) y float (para decimales)
suma_buena= float(num1) + float(num2)
print(suma_buena)