import os
import time
import globais

#Funções

def exibirMenu():
    animar2("Aguarde")
    print("===Padaria do Python===\n")
    print("1 - Vender")
    print("2 - Ver hitórico")
    print("3 - Sair\n")
    opcao = int(input("--Opção: "))
    return opcao

def vendas():
    print("===Vender===\n")
    descricao = input("-Descrição de pagamento: ")
    valor = float(input("-valor total da venda: "))
    print()
    if(valor > 0): 
        print("---Sucesso---")
        globais.saldo += valor
        globais.historico += f"{descricao}: {valor:.2f} €\n"
    else: print("---valor errado---")
    
    

def exibirhistorico():
    print("===Histórico===\n")
    print(f"Total de vendas: {globais.saldo:.2f} € \n")
    print(globais.historico)
    

    
# Funções Especiais
def limpa():
    if(os.name =="nt"): os.system("cls")
    else:(os.system("clear"))
def aguarde(tempo): time.sleep(tempo)

def animar(frase):
    tempo = 0.3
    limpa()

    print(frase, end="", flush=True)
    for i in range(3):
        print(".", end="", flush=True)
        aguarde(tempo)
    
    limpa()

def animar2(frase):
    tempo =0.1
    limpa()
    frase += "..."

    for letra in frase:
        print(letra, end="", flush=True)
        aguarde(tempo)
    limpa()

def animar3(frase):
    tempo =0.1
    limpa()

    for letra in frase:
        print(letra, end="", flush=True)
        aguarde(tempo)
    
    for i in range (3):
        print(".", end="", flush=True )
        aguarde(0.5)

def carrgueEnter():
    input('\nPressione ENTER para continuar...')