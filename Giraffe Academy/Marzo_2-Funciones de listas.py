#FUNCIONES DE LISTAS
#Vamos a partir de una lista de números y otra de palabras
números_primos= [2,3,5,7,9,11]
clones= ["Sarah", "Helena", "Cosima", "Alison", "Rachel"]

#1.Unir listas-función "extend"
clones.extend(números_primos)
print(clones)

#2. Añadir valores-función "append"
clones.append("MK") #OJO. Por defecto, te lo añade al final
print(clones)

#3. Añadir valor en una posición determinada-función "insert"
#Para esta necesitas introducir dos informaciones, el índice de la posición y el nombre de la variable.
clones.insert(1,"Beth")
print(clones)

#4. Quitar elementos-función "remove"
clones.remove("Rachel")
print(clones)

#5. Borrar lista-función "clear"
clones.clear()
print(clones)

#6. Quitar el último elemento-función "pop"
números_primos.pop()
print(números_primos)

clones= ["Sarah", "Helena", "Cosima", "Alison", "Rachel"]
print(clones)
#Comprobar si una variable está en la lista-función "index"
#Te devuelve el índice de tu valor, si es que está ahí dentro
print(clones.index("Alison"))
#print(clones.index("Krystal")) #te da un error porque no está

nombres= ["Pepa", "Pepo", "Pipa", "Pipa", "Popa", "Pupa"]

#7. Número de veces que aparece un elemento-función "count"
print(nombres.count("Pipa"))

#8. Ordenar alfabéticamente/ordinalmente-función "sort"
clones.sort()
print(clones)

#9. Dar la vuelta a la lista-función "reverse"
números_primos.reverse()
print(números_primos)

#10. Duplicar lista-función "copy"
nombres2= nombres.copy()
print(nombres2)