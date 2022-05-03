#Vamos a usar este fichero en Marzo_24.

#class ChefChino:
    #este chef hace lo mismo que el normal y más
    #def haz_pollo(self):
        #print("El chef hace un pollo")

    #def haz_ensalada(self):
        #print("El chef hace una ensalada")

    #def haz_plato_especial(self):
        #print("El chef hace rollitos de primavera") #su plato especial es otro

    #def haz_arroz_frito(self):
        #print("El chef hace arroz frito")

#Puedo crear una clase nueva y hacer copy paste o puedo HEREDAR.

from Chef import Chef

class ChefChino(Chef): #dentro de ChefChino uso las funciones de Chef

    def haz_arroz_frito(self):
        print("El chef hace arroz frito")
    #¿Qué pasa si quiero cambiar una de las funciones de la clase de la que heredo? La sobreescribes.
    def haz_plato_especial(self):
        print("El chef hace rollitos de primavera")


