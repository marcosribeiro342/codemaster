print("\n\n")
print("{:=^20}".format("Inicio") + "\n")


def indice(peso, altura):
    imc = peso / (altura ** 2)
    return imc


peso = float(input("Diga o seu peso em (kg): "))
altura = float(input("Diga a sua altura em (m): "))
indice_gord = indice(peso, altura)
print(f"o indice de gordura corporal é: {indice_gord:.1f}")


# peso_1 = 123
# altura_1 = 1.83
# imc_1 = peso_1 / (altura_1 ** 2)

# peso_2 = 100
# altura_2 = 1.73
# imc_2 = peso_2 / (altura_2 ** 2)

# peso_3 = 72
# altura_3 = 1.75
# imc_3 = peso_3 / (altura_3 ** 2)


print("\n" + "{:=^20}".format("Fim"))
print("\n\n")
