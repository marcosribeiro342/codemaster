import funcoes
from funcoes import *


limpa()

print("{:=^20}".format("inicio") +"\n" )
tempo = 0.75


nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
experiencia = input("Voce tem experiência em programação? ")
resultado = idade, experiencia


limpa()
print("A analizar",end="", flush=True)
aguarde(tempo)
print(".",end="", flush=True)
aguarde(tempo)
print(".",end="", flush=True)
aguarde(tempo)
print(".",end="", flush=True)
aguarde(tempo)
print(".",end="", flush=True)

limpa()
print("{:=^28}".format(" Ficha de Candidatura ") +"\n" )
print(f"Nome: ( {nome} )")
print(f"Idade: ( {idade} )")
print(f"Status da candidatura: ( {candidaturas(idade, experiencia)} )")



print("\n\n")
