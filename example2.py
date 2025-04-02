import example1 as exam

def main():
    edades = [3,5,7,9,11,13,15]
    edad_obj = exam.Edad(edades) 
    print(edad_obj.mostrar_media())

if __name__ == "__main__":
    main()