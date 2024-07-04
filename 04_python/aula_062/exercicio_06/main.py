import funcoes
from funcoes import *

limpa()

c = float(input("Digite uma temperatura em celsius: "))

print()

graus = input("Voce deseja converter para (k)elvin ou (F)ahrenheit? ")

if (graus.lower() == "k"):
    grausKelvin(c)
elif( graus.lower() == "f"):
    grausFahrenheit(c)
else:
    print("opção inválida")
                

print("\n" + "{:=^20}".format("Fim"))
print("\n\n")