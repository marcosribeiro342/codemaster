import funcoes
from funcoes import *


limpa()

print("==== Cálculo de Áreas com Funções ====")
print("=== Escolha uma opção ===")
print("(t) para triângulos")
print("(r) para retangulos")
print("(c) para círculo")
print("")
opcao = input("Opcao: ")

animar("A analisar")

if(opcao.lower() == "t"):
    base = float(input("Digite a sua base: "))
    altura = float(input("-Digite a sua altura: "))
    resultado = areaTriangulo(base, altura)

elif(opcao.lower() == "r"):
    base = float(input("Digite a sua base: "))
    altura = float(input("-Digite a sua altura: "))
    resultado = areaRetangulo(base, altura)

elif(opcao.lower() == "c"):
    raio = float(input("-Digite o seu raio: "))
    resultado = areaCirculo(raio)

else: resultado = "--- Opção Inválida ---"

animar("A analisar")

print("==== Cálculo de Áreas com Funções ====")
print()
print(resultado)






print("\n\n")
