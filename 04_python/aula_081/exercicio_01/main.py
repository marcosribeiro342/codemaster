from funcoes import *
from Usuario import *
import globais



limpa()




print("=== Lista original ===")
for u in globais.usuarios: u.toString()
print()

login_digitado = input("-Digite o login que deseja buscar: ")

if(verificarLogin(login_digitado)):
    print("\n---Encontrado---")

else:
    print("\n--- LOGIN INVALIDO ---")


print("\n\n")
