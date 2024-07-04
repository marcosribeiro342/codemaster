print("\n\n")
print("{:=^20}".format("Inicio") + "\n")


def indice():
    nome = input("qual o seu nome? ")
    peso = float(input("Diga o seu peso em (kg): "))
    altura = float(input("Diga a sua altura em (m): "))
    imc_1 = peso / (altura ** 2)
    print(f"o indice de gordura corporal do(a) {nome} é: {imc_1:.1f}")

indice()

print("\n" + "{:=^20}".format("Fim"))
print("\n\n")