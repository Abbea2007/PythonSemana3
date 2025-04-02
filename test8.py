"""Escribe un programa que tome una lista de cadenas y
 determine cuál es la más larga y cuál es la más corta.
"""

lista_cadenas = []

def pedir_cadena():
    cadena = input("Ingrese la cadena: ")
    cadena_separada = cadena.split(",")
    lista_cadenas.extend(cadena_separada)

cadena_larga = ""
cadena_corta = lista_cadenas[0]

def calcular_longitud(lista,larga, corta):
   
   for string in lista:
     if len(string) > len(larga):
        larga = string
     elif len(string) < len(corta):
        corta = string

pedir_cadena()

resultado = calcular_longitud(lista_cadenas, cadena_larga, cadena_corta)
print(f"La cadenas mas larga es: {cadena_larga} y la cadena mas corta es {cadena_corta}")           