#CALCULADORA MEJOR QUE LA BÁSICA
num1= float(input("Introduce el primer número: ")) #con el float me aseguro de que es un número
op= input("Introduce un operador: ")
num2= float(input("Introduce el segundo número: "))

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Operador no válido")

