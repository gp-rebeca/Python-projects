#CLASES Y OBJETOS
#Hacen tus programas más organizados y poderosos.
#Quiero representar un estudiante. En el archivo "estudiante" tengo el perfil de un estudiante.

from estudiante import estudiante #de este fichero quiero importar esta clase
estudiante1= estudiante("Anselmo", "Matemáticas", 3.1) #aquí dentro pongo el nombre, el grado, la nota y si está en probation
estudiante2= estudiante("Luisa", "Física", 4)
print(estudiante1.nombre)
print(estudiante2.nota)

#Cuando creamos un studiante, lo estamos pasando por la función init.
#Con las clases podemos representar entindades y sus atributos.