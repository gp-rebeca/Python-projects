#TEST OPCIÓN MÚTLIPLE
from preguntas import Pregunta
preguntas_opciones=[
    "¿De qué color son los limones?\n(a) Rosas\n(b) Azules\n(c) Amarillos\n\n",
    "¿De qué color son las fresas?\n(a) Rojas\n(b) Negras\n(c) Moradas\n\n",
    "¿De qué color son los melocotones?\n(a) Naranjas\n(b) Verde moco\n(c) Rojos\n\n"
]

preguntas=[
    Pregunta(preguntas_opciones[0], "c"), #la respuesta a la primera pregunta es la c
    Pregunta(preguntas_opciones[1], "a"),
    Pregunta(preguntas_opciones[2], "a")
]

def run_test(preguntas):
    score=0 #quiero ir incrementando mi puntuación
    for pregunta in preguntas:
        respuesta = input(pregunta.pregunta)
        if respuesta == pregunta.respuesta:
            score += 1
    print("Tienes "+ str(score) + "/" + str(len(preguntas)) + " aciertos.")

run_test(preguntas)

