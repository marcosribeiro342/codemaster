import os

#Funções

def digitarTecla(caracter):
    print(f" O caracter digitado foi: ({caracter})\n")

# Funções Especiais
def limpa():
    if(os.name =="nt"): os.system("cls")
    else:(os.system("clear"))