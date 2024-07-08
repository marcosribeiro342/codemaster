import os

#Funções
def lerNumeroPositivo():
    num = float(input("Digite um número: "))
    if num >= (0):
        print("É POSITIVO")
    else:
        print("É NEGATIVO")
   

# Funções Especiais
def limpa():
    if(os.name =="nt"): os.system("cls")
    else:(os.system("clear"))