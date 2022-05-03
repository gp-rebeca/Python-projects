#DICCIONARIO
#Nos permite almacenar información en key value pairs. Si quiero acceder a esta información, me puedo referir a la key.
#Se pone el nombre= llaves. Lo que vaya entre las llaves es lo que hace el diccionario.
convertir_meses = {
    "Ene": "Enero", #key:value. Las keys tienen que ser diferentes
    "Feb": "Febrero",
    "Mar": "Marzo",
    "Abr": "Abril",
    "May": "Mayo",
    "Jun": "Junio",
    "Jul": "Julio",
    "Ago": "Agosto",
    "Sept": "Septiembre",
    "Oct": "Octubre",
    "Nov": "Noviembre",
    "Dic": "Diciembre",
}

print(convertir_meses["Nov"]) #nos devuelve la palabra asociada
print(convertir_meses.get("Mar"))
print(convertir_meses.get("Cua", "Clave no válida"))

#Las keys pueden ser numeritos
convertir_meses2= {
    1: "Enero", #key:value. Las keys tienen que ser diferentes
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre",
}

print(convertir_meses2[8])