import os

#Funções
def lerNumero():
    num = float(input("Digite um número: "))
    if num >= (10):
        print("É MAIOR QUE 10")
    else:
        print("NÃO É MAIOR QUE 10")
   

# Funções Especiais
def limpa():
    if(os.name =="nt"): os.system("cls")
    else:(os.system("clear"))