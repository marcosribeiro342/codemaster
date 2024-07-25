from funcoes import *

limpa()

while(True):
    
    opcao = exibirMenu()

    animar2("Aguarde")

    if(opcao ==1):registarColaborador()
    elif(opcao ==2):editarColaborador()
    elif(opcao ==3):apagarColaborador()
    elif(opcao ==4):listarColaboradores(True)
    elif(opcao ==0):
        animar2("A sair")
        break
    else:
        print("--- Dados Inválidos ---")
    
    
    carrgueEnter()


print("\n\n")
