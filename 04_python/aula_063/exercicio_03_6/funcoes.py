import os

#Funções

def dimensoesDoRetangulo():
    base = float(input("Digite a base do seu retângulo: "))
    altura = float(input("Digite a altura do seu retângulo: "))
    area = base * altura
    print(f" A area do seu retângulo é: ({area:.2f})\n")

# Funções Especiais
def limpa():
    if(os.name =="nt"): os.system("cls")
    else:(os.system("clear"))