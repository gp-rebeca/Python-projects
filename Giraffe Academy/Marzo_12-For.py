#BUCLE FOR
for letra in "Giraffe Academy": #variable que va a tener un valor diferente cada vez que se realimente el bucle
    print(letra) #te va salir igual poniendo letra o poniendo culo. Ciéntificamente testado

clones= ["Sarah", "Cosima", "Alison", "Helena"]
print(len(clones)) #te dice el número de clones, length
for clon in clones:
    print(clon) #igualmente poniendo culo nos devuelve los clones. Esa primera palabra para el llamamiento da igual.

for índice in range(10): #rango del 0 al 9
    print(índice)

for índice in range(3,10): #sin incluir el 10
    print(índice)

for índice in range(len(clones)): #los índices de los clones del 0 al último clon
    print(índice)

for índice in range(len(clones)): #los índices de los clones del 0 al último clon
    print(clones[3])

for índice in range(5):
    if índice==0:
        print("Primera iteración")
    else:
        print("No primera iteración")








