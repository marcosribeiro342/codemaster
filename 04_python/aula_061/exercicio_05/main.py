print("\n\n")
print("{:=^20}".format("Inicio") + "\n")

numero = int(input('Digite um número: '))
numero_1 = numero % 2

print()


if (numero_1 == 0):
    print("É par")

else:
    print("É impar")

print("\n" + "{:=^20}".format("Fim"))
print("\n\n")