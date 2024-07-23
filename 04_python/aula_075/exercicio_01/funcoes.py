import os
import time
import globais
#Funções

def exibirMenu():
    animar2("Aguarde")
    print("=== Cadastro de Pessoas ===\n")
    print("1 - cadastrar uma nova pessoa")
    print("2 - Editar pessoa")
    print("3 - Apagar pessoa\n")
    print("4 - Listar todas as pessoas\n")
    print("0 - Sair\n")
    return int(input("-- Opção: "))

def cadastrarPessoas():
    print("--- Cadastro de uma nova pessoa ---\n")
    novo_nome = input("- Digite o nome da pessoa: ")
    if(not(novo_nome in globais.pessoas)):
        globais.pessoas.append()
        print("\n --- Sucesso --")

def editarPessoas():
    print("--- Edição da pessoa ---\n")
    listarPessoas(False)
        
    id = int(input("\n-Digite o código da pessoa que queres editar: ")) 
    if(id >= 0 and id < len(globais.pessoas)):
        novo_nome = input(f"\n-Digite nome para substituir ({globais.pessoas[id]}): ")
        if(not(novo_nome in globais.pessoas)):
            globais.pessoas[id] = novo_nome
            print("\n--- Sucesso ---")
    else:
        print("\n--- CÓDIGO INVÁLIDO ---")

def apagarPessoas():
    print("--- Apagar Pessoa ---\n")
    listarPessoas(False)

    id = int(input("\n-Digite o código da pessoa que queres apagar: ")) 
    if(id >= 0 and id < len(globais.pessoas)):
        apagar = globais.pessoas.pop(id)
        print(f"\n---({apagar}) Apagado(a) com sucesso ---")
        
        
    else:
        print("\n--- CÓDIGO INVÁLIDO ---")


def listarPessoas(com_titulo):
    if(com_titulo):print("--- Lista das pessoas ---\n")
    for i in range(len(globais.pessoas)):
        print(f"ID: ( {i} ) - Nome:  ( {globais.pessoas[i]} )")

    




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