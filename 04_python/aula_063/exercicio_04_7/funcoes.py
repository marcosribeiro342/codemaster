import os

#Funções

def anosDeUmaPessoa():
    nome = input("Diga-me o seu nome: ")
    anos = int(input("Digite os seus anos: "))
    meses = int(input("Digite os seus meses: "))
    dias = int(input("Digite os seus dias: "))
    total_dias = (anos * 365) + (meses * 30) + dias
    print(f" O total de dias do(a) {nome}, é ({total_dias})\n")

# Funções Especiais
def limpa():
    if(os.name =="nt"): os.system("cls")
    else:(os.system("clear"))