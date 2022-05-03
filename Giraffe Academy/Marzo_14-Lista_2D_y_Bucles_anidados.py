#LISTA 2D Y BUCLES ANIDADOS
#Vamos a hacer una lista de listas, o sea, una lista con listas dentro
red_de_números= [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
] #Tiene 4 elementos y cada elemento es a su vez una lista (cuatro filas y tres columnas). Como una matriz

print(red_de_números[1][2]) #el primer número es la fila y el segundo, la columna. RECUERDA QUE TODO SE EMPIEZA A CONTAR DESDE 0

#Bucle anidado es un bucle dentro de otro.

for fila in red_de_números:
    for columna in fila:
        print(columna)



