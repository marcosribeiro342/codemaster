import funcoes
from funcoes import *
limpa()

frase = input("-Digite uma string: ")
print()

for letra in frase:
    print(letra)
    aguarde(0.2)
    if(letra.lower() == "x"): break


print("\n\n")