import os

#Funções

def salario_funcionario():
    sal_funcionario1 = float(input("Digite o seu salario: "))
    aumento = sal_funcionario1 * 1.1
    diminuido = sal_funcionario1 * 0.9
    print(f"O seu salário depois de reajustado ser: ({aumento:.2f} € ou {diminuido:.2f} €) \n")

    

# Funções Especiais
def limpa():
    if(os.name =="nt"): os.system("cls")
    else:(os.system("clear"))