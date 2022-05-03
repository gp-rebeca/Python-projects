#TUPLAS
#Contenedor para almacenar información. Algo diferente a las listas. SON INMUTABLES. NO SE PUEDEN MODIFICAR.
#Pones nombre = () y ya
coordenadas= (4, 5)
#Para acceder a los elementos de la tupla, se llaman por sus índices entre corchetes, empezando por el 0.
print(coordenadas[0])
#Si intento cambiar un elemento, me da error
#coordenadas[1]=10
#print(coordenadas)
#
#Diferencias entre listas y tuplas:
##1. Puedes modificar las listas, las tuplas no
##2. Tuplas son mejores para almacenar datos que no vas a cambiar
##3. Puedo hacer una lista de tuplas
puntos= [(4,5), (3,9), (7,2)]
print(puntos)
##4. Normalmente vas a usar listas
