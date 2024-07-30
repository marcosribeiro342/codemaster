from funcoes import *

limpa()

init()

while(True):
    
    opcao = exibirMenu()

    animar2("Aguarde")

    if(opcao ==1):registarProdutos()
    elif(opcao ==2):editarProdutos()
    elif(opcao ==3):apagarProduto()
    elif(opcao ==4):listarProdutos(True)
    elif(opcao ==5):venderProduto()
    elif(opcao ==6):listarVendas(True)
    elif(opcao ==0):
        animar2("A sair")
        break
    else:
        print("--- Dados Inválidos ---")
    
    
    carrgueEnter()


print("\n\n")
