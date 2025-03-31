import example1

def main():
    edades = [3,5,7,9,11,13,15]
    edad_obj = example1.Edad(edades)
    print(edad_obj.mostrar_media())

if __name__ == "__main__":
    main()