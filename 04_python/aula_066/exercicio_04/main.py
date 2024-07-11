import funcoes
from funcoes import *
limpa()

resposta = ""
r_1 = ""

while(resposta.lower() != "nao"):
    resposta = input("Queres tirar a carta de condução? ")
    if(resposta.lower() == "sim"):
        print("estudar para o teste")
        while(r_1.lower() != "sim"):
            r_1 = input("Voce passou no teste? ")
            if(r_1.lower() == "nao"):
                print("estudar para o teste")

            else:print("Parabéns!!")
                   

print("Anda de transportes publicos")


print("\n\n")
