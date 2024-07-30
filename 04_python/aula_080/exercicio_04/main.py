from funcoes import *
from Usuario import *
import random


limpa()



while(True):
    print("=== Lista original ===")
    for u in globais.usuarios: u.toString()
    print()

    login_digitado = input("- Login: ")
    senha_digitado = input("- Senha: ")

print("\n\n")
