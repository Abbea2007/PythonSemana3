"""Escribe una función que reciba una cadena y la retorne sin
    vocales si su longitud es impar; si es par, la retorna sin consonantes."""

cadena = "Hola mi nombre es carlos"

vocales = "aeiou"
consonantes = "abcdefijklmnopqrstuvwxys"

def eliminar_con_vocal(caden, vowels, consonents):
    for string in caden:
        if len(string) % 2 == 1:  # Si la longitud es impar, eliminar vocales
            for vocals in vowels:
                string = string.replace(vocals, "")
            return string  # Retorna después de eliminar todas las vocales
        elif len(string) % 2 == 0:  # Si la longitud es par, eliminar consonantes
            for conson in consonents:
                string = string.replace(conson, "")
            return string  # Retorna después de eliminar todas las consonantes
                    
                    
                                   
print(eliminar_con_vocal(cadena, vocales, consonantes))
