#leer x cantidad de edad y calcular la media

class Edad:
    def __init__(self, edades):
        self.edades = edades
    def calcular_media(self):
        return sum(self.edades) / len(self.edades)
    def mostrar_media(self):
        media = self.calcular_media()
        return f"La media de las edades es: {media: .2f}"
    
def main():
    edades = []

    while True:
        try:
            edad = int(input("Ingrese una edad (o -1 para terminar)"))
            if edad == -1:
                break
            edades.append(edad)
        except ValueError:
            print("pOr favor, ingrese un numero valido.")
    
    edad_obj = Edad(edades)
    print(edad_obj.mostrar_media())

if __name__ == "__main__":
    main()