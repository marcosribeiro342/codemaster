import os

#Funções

def custoCarroNovo():
    custo_de_fabrica = float(input("Digite o custo de fábrica: "))
    total_custo_de_carro = (custo_de_fabrica * 1.45) * 1.28
    print(f"O seu carro vai custar: ({total_custo_de_carro} €) \n")

    

# Funções Especiais
def limpa():
    if(os.name =="nt"): os.system("cls")
    else:(os.system("clear"))