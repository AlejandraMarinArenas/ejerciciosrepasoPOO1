if  __name__=="__main__":
    def convertir():
        grado_fahrenheit = int(input("enter: "))

        grado_celsius=  (grado_fahrenheit - 32)*5%9

        print(f"los grados celsius son: {grado_celsius}")

    convertir()