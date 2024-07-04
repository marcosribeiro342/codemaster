print("\n\n")
print("{:=^20}".format("Inicio") + "\n")

def calcularImc(peso, altura):
    imc = peso / (altura ** 2)
    print(f"IMC: ( {imc:.1f} ) \n")

peso = float(input("Digite o seu peso em (Kg): "))
altura = float(input("Digite a sua altura em (m): "))

calcularImc(peso,altura)

print("\n" + "{:=^20}".format("Fim"))
print("\n\n")