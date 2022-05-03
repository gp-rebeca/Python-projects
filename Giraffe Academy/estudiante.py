#Fichero que voy a usar en Marzo_21 y Marzo 23.
class estudiante:

    def __init__(self, nombre, grado, nota): #initialized function. Esto es el perfil del estudiante.
        self.nombre= nombre #el nombre del estudiante va a ser igual al nombre que le pasemos
        self.grado= grado
        self.nota = nota

    def en_lista_honor(self):
        if self.nota>=8.5:
            return True
        else:
            return False

