"""Escribe un programa que tome una lista de cadenas y
genere una nueva lista con las cadenas invertidas.
"""

lista_cadenas = []

def pedir_cadena():
    cadenas = input("Ingrese la cadena: ")
    cadena_separada = cadenas.split(",")
    lista_cadenas.extend(cadena_separada)


def invertir_cadena(lista):
    new_list = []
    for string in lista:
        new_list.append(string.strip()[::-1])
    return new_list

pedir_cadena()
resultado = invertir_cadena(lista_cadenas)
print(resultado)
    