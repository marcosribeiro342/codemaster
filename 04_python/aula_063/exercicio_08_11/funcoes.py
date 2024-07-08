import os

#Funções

def salarioDoVendedor():
    carros = int(input("Digite quandos carros vendeu: "))
    valor_vendas = float(input("Digite o valor total das vendas efetuadas: "))
    salario = float(input("Digite o seu salário: "))
    carro_vendido = float(input("Digite o valor que recebe por cada carro: "))
    total_salario = salario + (carros * carro_vendido) + (valor_vendas * 0.05)
    print(f"o salario do vendedor é: ({total_salario:.2f} €) \n")

    

# Funções Especiais
def limpa():
    if(os.name =="nt"): os.system("cls")
    else:(os.system("clear"))