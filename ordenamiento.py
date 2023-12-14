import random

def generar(lista):
    for i in range(10):
        lista[i] = random.randint(1, 100)
        if i == 0:
            print(f"Lista original: [{lista[i]}, ", end="")
        elif i == 9:
            print(f"{lista[i]}]")
            print()
        else:
            print(f"{lista[i]}, ", end="")

def ascendente(lista):
    for i in range(10):
        for j in range(9):
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux

    for i in range(10):
        if i == 0:
            print(f"Lista en orden ascendente: [{lista[i]}, ", end="")
        elif i == 9:
            print(f"{lista[i]}]")
            print()
        else:
            print(f"{lista[i]}, ", end="")

def descendente(lista):
    for i in range(10):
        for j in range(9):
            if lista[j] < lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux

    for i in range(10):
        if i == 0:
            print(f"Lista en orden descendente: [{lista[i]}, ", end="")
        elif i == 9:
            print(f"{lista[i]}]")
            print()
        else:
            print(f"{lista[i]}, ", end="")

# Código principal
lista = [0] * 10
generar(lista)
ascendente(lista)
descendente(lista)