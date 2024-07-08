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

def descontar10(valor):
    resultado = valor * 0.9
    print(f"O valor em promoção é ({resultado:.2f} €)")

def descontar10ComReturn(valor):
    resultado = valor * 0.9
    return resultado
    
   

# Funções Especiais
def limpa():
    if(os.name =="nt"): os.system("cls")
    else:(os.system("clear"))