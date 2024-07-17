import os
import time
import globais

#Funções

def exibirMenu():
    animar2("Aguarde")
    print("===MULTIBANCO===\n")
    print(f"Bem vindo {globais.nome}")
    print(f"Saldo atual: {globais.saldo:.2f} €\n")
    print("1 - Levantar")
    print("2 - Depositar")
    print("3 - Pagamentos\n")
    print("4 - Sair\n")
    opcao = int(input("--Opções: "))
    return opcao

def depositar():
    print("===Depósitos===\n")
    valor = float(input("-Digite o valor depositado "))
    print()
    if(valor > 0): 
        print("---Sucesso---")
        globais.saldo += valor
    else: print("---valor errado---")
    print(f"Novo saldo: {globais.saldo:.2f} €")
    print()
    

def levantar():
    print("===Levantamentos===\n")
    valor = float(input("-Digite o valor levantado: "))
    print()
    if(valor > 0 and valor <= globais.saldo): 
        print("---Sucesso---")
        globais.saldo -= valor
    else: print("---valor errado---")
    print(f"Novo saldo: {globais.saldo:.2f} €")
    print()

def pagamentos():
    print("===Pagamentos===\n")
    input("-Descrição de pagamento: ")
    valor = float(input("-Digite o valor levantado: "))
    print()
    if(valor > 0 and valor <= globais.saldo): 
        print("---Sucesso---")
        globais.saldo -= valor
    else: print("---valor errado---")
    print(f"Novo saldo: {globais.saldo:.2f} €")
    print()


    
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