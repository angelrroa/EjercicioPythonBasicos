def maquina_alimentos():
    print("¿Qué producto desea comprar?")
    print("A --------------------> $270")
    print("B --------------------> $340")
    print("C --------------------> $390")
    print("Ingrese solo monedas de $10, $50, $100")

    producto = input("Ingrese el producto: ")
    acumulado = 0

    if producto == "A":
        while acumulado < 270:
            dinero = int(input("Ingrese el dinero: "))
            if dinero == 10 or dinero == 50 or dinero == 100:
                acumulado += dinero
            else:
                print("Moneda no válida, intenta de nuevo")

        vuelto = acumulado - 270

    elif producto == "B":
        while acumulado < 340:
            dinero = int(input("Ingrese el dinero: "))
            if dinero == 10 or dinero == 50 or dinero == 100:
                acumulado += dinero
            else:
                print("Moneda no válida, intenta de nuevo")

        vuelto = acumulado - 340

    elif producto == "C":
        while acumulado < 390:
            dinero = int(input("Ingrese el dinero: "))
            if dinero == 10 or dinero == 50 or dinero == 100:
                acumulado += dinero
            else:
                print("Moneda no válida, intenta de nuevo")

        vuelto = acumulado - 390

    print("Su vuelto:")

    if vuelto == 0:
        print("0")
    else:
        while vuelto >= 100:
            print("100")
            vuelto -= 100

        while vuelto >= 50:
            print("50")
            vuelto -= 50

        while vuelto >= 10:
            print("10")
            vuelto -= 10


# Llamada a la función
maquina_alimentos()