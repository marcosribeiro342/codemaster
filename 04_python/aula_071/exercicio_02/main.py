import funcoes
from funcoes import *
import globais

limpa()

while(True):

    opcao =exibirMenu()
    
    animar2("Aguarde")

    if(opcao == 1): vendas()
    elif(opcao == 2):exibirhistorico()
    elif(opcao == 3):
        animar2("A sair")
        break
    else:
        print("---Opção Inválida----")
        

    carrgueEnter()


print("\n\n")

