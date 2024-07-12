import funcoes
from funcoes import *
limpa()

resposta =""
tentativas = 1
carta = input("Queres tirar a carta de condução? ")
limpa()

if (carta.lower() == "sim" ):
    while (resposta.lower() != "sim"):
        print()
        print(f"Estude para o teste ({tentativas}) ")
        resposta = input(f"Passou no teste ({tentativas})? ")
        tentativas += 1
    print()
    print("Parabéns")
    print(f"Voce foi aprovado no teste ({tentativas - 1})")
    
elif (carta.lower() == "nao"):print( "Utilize transportes publicos")

else:
    print("opçao invalida")


print("\n\n")
