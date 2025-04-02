"""Escribe un programa que recorra una lista de cadenas 
y reemplace todas las vocales por un asterisco (*).
"""

lista_cadenas = []

def pedir_cadenas():
    cadena = input("Ingrese la cadena: ")
    cadena_separada = cadena.split(",")
    lista_cadenas.extend(cadena_separada)

vocales_reemplazar = "aeiou"
new_character = "*"

def borrar_vocales(lista, vocal_vieja, nuevo_caracter):
    new_list = []
    for string in lista:
        for x in vocal_vieja:
            string = string.replace(x, nuevo_caracter)
        new_list.append(string.strip())
    return new_list

pedir_cadenas()
resultado = borrar_vocales(lista_cadenas, vocales_reemplazar, new_character)
print(f"Las vocales reemplazadas por {new_character} son: {resultado}")
