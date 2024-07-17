import funcoes
from funcoes import *
import globais

limpa()

while(True):

    opcao =exibirMenu()
    
    animar2("Aguarde")

    if(opcao == 1): 
        levantar()
    elif(opcao == 2):
        depositar()
    elif(opcao == 3):
        pagamentos()
    elif(opcao == 4):
        animar2("A sair")
        break
    else:
        print("---Opção Inválida----")
        

    carrgueEnter()


print("\n\n")
