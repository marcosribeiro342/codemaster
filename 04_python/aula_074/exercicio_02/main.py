from funcoes import *
limpa()

while(True):
    
    opcao = exibirMenu()

    animar2("Aguarde")

    if(opcao ==1):cadastrarPessoas()
    elif(opcao ==2):editarPessoas()
    elif(opcao ==3):apagarPessoas()
    elif(opcao ==4):listarPessoas()
    elif(opcao ==0):
        animar2("A sair")
        break
    else:
        print("--- Dados Inválidos ---")
    
    carrgueEnter()

print("\n\n")
