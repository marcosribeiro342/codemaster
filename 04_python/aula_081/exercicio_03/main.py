from funcoes import *

limpa()



while(True):
    limpa()
    print("=== Login ===\n")

    login_digitado = input("- Login: ")
    senha_digitada = input("- Senha: ")

    if(verificarLogin(login_digitado,senha_digitada)):
        print("\n--- SUCESSO! ---")
        break
    else:
        print("\n--- LOGIN INVALIDO ---")
        
    carrgueEnter()



print("\n\n")
