import os

#Funções
def exibirMensagens():
    print("mensagem 1")
    print("mensagem 2")
    print("mensagem 3")

def calcDobro():
    x = float(input("Digite um numero "))
    dobro = x * 2 
    print(f" O dobro de ({x}) é ({dobro}) \n")

def calcTriplo(valor):
    triplo = valor * 3 
    print(f" O triplo de ({valor}) é ({triplo}) \n")

# Funções Especiais
def limpa():
    if(os.name =="nt"): os.system("cls")
    else:(os.system("clear"))