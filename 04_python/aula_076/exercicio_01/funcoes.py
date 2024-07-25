import os
import time
#Funções

def novaPessoa(nome, idade, morada):
    pessoa_individual =[nome,idade,morada]
    return pessoa_individual

def toString(i,pessoa_individual):
    print(f"{i+1} - {pessoa_individual[0]} (Idade: {pessoa_individual[1]}) [Morada:{pessoa_individual[2]}]")



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