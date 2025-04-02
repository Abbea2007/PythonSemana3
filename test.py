"""Escribe un programa que recorra una lista de cadenas y cuente cuántas palabras 
tiene cada cadena. Almacena los resultados en una nueva lista."""

lista_cadenas = []

def pedir_cadena():
    cadena = input("Ingrese la cadena para contar las palabras: ")
    lista_cadenas.append(cadena)
    
def contar_palabras(lista):
    new_lista = []
    for string in lista:
        resultado = len(string.split())
        new_lista.append(resultado)
    return new_lista

pedir_cadena()
respuesta = contar_palabras(lista_cadenas)

print(f"La cadena tiene {respuesta} palabras")
