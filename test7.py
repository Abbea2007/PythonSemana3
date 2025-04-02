"""Escribe un programa que tome una lista de cadenas y 
devuelva una nueva lista donde cada cadena tenga su primera letra en mayúscula.
"""

lista_cadenas = []

def pedir_cadena():
    cadena = input("Ingrese la cadena: ")
    cadena_separada = cadena.split(",")
    lista_cadenas.extend(cadena_separada)

def first_mayus(lista):
    new_list = []
    for string in lista:
        result = string.strip().capitalize()
        new_list.append(result.strip())
    return new_list

pedir_cadena()
resultado = first_mayus(lista_cadenas)
print(f"La cadena con su primer letra en mayuscula es: {resultado}")
