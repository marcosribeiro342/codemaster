from funcoes import *
import globais



limpa()



while(True):
    print("=== Lista original ===")
    for u in globais.usuarios: u.toString()
    print()

    login_digitado = input("- Login: ")
    senha_digitada = input("- Senha: ")

    if(verificarLogin(login_digitado,senha_digitada)):
        print("\n--- SUCESSO! ---")
    else:
        print("\n--- LOGIN INVALIDO ---")



print("\n\n")
