if __name__=="__main__":
    lista=[]
    for x in range(7):
        valor=int(input("Ingrese valor: "))
        lista.append(valor)

    mayor=lista[0]
    menor=lista[0]
    for x in range(1,7):
        if lista[x]>mayor:
            mayor=lista[x]
        elif lista[x]<menor:
            menor=lista[x]

    print("Lista completa")
    print("---------------------")
    print(lista)
    print("---------------------")
    print("Mayor de la lista")
    print(mayor)
    print("---------------------")
    print("Menor de la lista")
    print(menor)

