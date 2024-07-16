import funcoes
from funcoes import *
limpa()

tentativas= 1
while(True):
    numero = int(input("-Digite um número inteiro: "))
    if(numero % 5 == 0): break
    tentativas += 1
    if(tentativas > 5): break


print("\n\n")

if(tentativas > 5): print("Ultrapassou o numero de tentativas")
else: print("Parabéns!")
