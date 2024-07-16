import funcoes
from funcoes import *
limpa()

print("------Break no While---------")
print()
tentativas= 1
while(True):
    encerrar = input(f"-Voce deseja terminar o loop WHILE na tentativa({tentativas}/5)?")
    if(encerrar == "sim"): break
    tentativas += 1
    if(tentativas > 5): break

print()

if(tentativas > 5): print("Ultrapassou o numero de tentativas")
else: print("Nao ultrapassou o numero de tentativas")

print()
print("------Break no for---------")
print()

for i in range(1,6):
    acabar = input(f"-Voce deseja terminar o loop FOR na tentativa({i}/5)?")
    if(acabar.lower() == "sim"):break
    # if(i > 5): break

print()

if(i == 5 and acabar.lower() != "sim"): print("Ultrapassou o numero de tentativas")
else: print("Nao ultrapassou o numero de tentativas")


print("\n\n")
