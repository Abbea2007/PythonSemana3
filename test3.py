"""Escribe un programa que recorra una lista de cadenas y genere 
una nueva lista con solo las cadenas que comienzan con una letra específica.
"""

lista_cadenas = []

def pedir_cadena():
    cadena = input("Ingrese la cadena: ")
    cadena_separada = cadena.split(",")
    lista_cadenas.extend(cadena_separada)
    
caracter_espec = "H"

def specific_letter(lista, caracter):
    new_list = []
    for string in lista:
        if string.strip()[0] == caracter:
            new_list.append(string.strip())
    return new_list


pedir_cadena()
resultado = specific_letter(lista_cadenas, caracter_espec)

print(f"la cadena es: {resultado}")



