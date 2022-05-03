#HERENCIA
#Crear una clase a partir de otra y heredar sus datos.

from Chef import Chef #Pero esta clase de chef es un muermo. Quiero hacer una más guay. Quiero un chef de comida china.
from ChefChino import ChefChino
myChef= Chef()
myChef.haz_pollo()
myChef.haz_plato_especial()

myChefChino= ChefChino()
myChefChino.haz_arroz_frito()
myChefChino.haz_plato_especial()



