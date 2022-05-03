#LISTAS
#(Muy similar a matrices en matlab).
#Pones nombre = corchetes y ya sabe que quieres almacenar información.
#Vamos a hacer una lista de algunos clones de Orphan Black
clones= ["Sarah", "Beth", "Cosima", "Alison", "Rachel"]
#En las listas puedo almacenar varios valores. Puedes almacenar tanto palabras (strings) como números.
#Para acceder a diferentes valores de la lista, me puedo referir a ellos con los índices de la posición que ocupan
# (como en las matrices), empezando por el número 0. Si usas índices negativos, empieza numerando por el final de la
# lista, siendo el último valor el índice -1.
print(clones)
print(clones[0]) #para acceder a Sarah
print(clones[-2])
#También puedes seleccionar desde un valor a otro con "índice:".
print(clones[1:]) #esto te escupe los clones no fértiles
#Para modificar valores, selecciono el valor y lo igualo a su nuevo valor.
clones[4]= "Katja"
print(clones[4])



