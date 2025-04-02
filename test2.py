"""Escribe un programa que recorra una lista de cadenas y 
cree una nueva lista con solo aquellas que contengan un 
número específico de caracteres (por ejemplo, más de 5 caracteres)."""

lista_cadenas = []

def pedir_cadena():
    cadena = input("Ingrese la cadena: ")
    cadena_separada = cadena.split(",")
    lista_cadenas.extend(cadena_separada)

def word_caracter(lista):
    new_list = []
    for string in lista:
        if len(string) >= (5 + 1):
            new_list.append(string.strip())
    return new_list

pedir_cadena()
respuesta = word_caracter(lista_cadenas)
print(f"Las palabras que tienen mas de 5 caracteres son {respuesta}")