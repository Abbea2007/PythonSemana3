"""Escribe un programa que tome una lista de cadenas y elimine todas las vocales de cada una.
"""

lista_cadenas = []

def pedir_cadena():
    cadena = input("Ingrese la cadena: ")
    cadena_separada = cadena.split(",")
    lista_cadenas.extend(cadena_separada)

vowels = "aeiou"

def eliminar_vocales(lista,vocales):
    new_list = []
    for string in lista:
        for vocal in vocales:
            string = string.replace(vocal, "")
        new_list.append(string.strip())
    return new_list

pedir_cadena()
resultado = eliminar_vocales(lista_cadenas, vowels)
print(f"La cadena sin vocales es: {resultado}")

        
