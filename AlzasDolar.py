def mayor_alza(valor_dolar, dias):
    alzas = [0] * dias

    for i in range(dias):
        if dias == 1:
            alzas[i] = 0
        else:
            if i != dias - 1:
                alza = valor_dolar[i + 1] - valor_dolar[i]
                alzas[i] = alza

    for i in range(dias):
        for j in range(dias - 1):
            if alzas[j] < alzas[j + 1]:
                aux = alzas[j]
                alzas[j] = alzas[j + 1]
                alzas[j + 1] = aux

    valor_mayor_alza = alzas[0]
    return valor_mayor_alza


# Algoritmo principal
dias = int(input("¿Cuántos días desea registrar? "))
valor_dolar = [0] * dias

for i in range(dias):
    vdol = float(input(f"Registre el valor del día {i + 1}: "))
    valor_dolar[i] = vdol

print("\nValores registrados:")
for i in range(dias):
    print(f"Día {i + 1}: {valor_dolar[i]}")

mayor_alza_valor = mayor_alza(valor_dolar, dias)

if mayor_alza_valor == 0 and dias != 1:
    print("No hubo alzas")
else:
    print(f"La mayor alza fue de {mayor_alza_valor} dólares")