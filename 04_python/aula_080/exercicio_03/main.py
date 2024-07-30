from funcoes import *
from Pessoa import *
import random


limpa()

pessoas = []



pessoas.append(Pessoa("Marcos Ribeiro", 16, "Vila real", 1111))
pessoas.append(Pessoa("Joao Teixeira", 10, "Braga", 2222))
pessoas.append(Pessoa("Rita Ferraz", 6, "Porto", 3333))
pessoas.append(Pessoa("Tomas Oliveira", 8, "Coimbra", 4444))
pessoas.append(Pessoa("Rui Teixeira", 13, "Leiria", 555))

print("=== Lista Original ===\n")

for a in pessoas: 
    a.toString()

print()

pessoas[0].completarAnos()
pessoas[2].completarAnos()
pessoas[4].completarAnos()

print()

pessoas[1].mudar("Lisboa")
pessoas[3].mudar("Santarém")

print()

print("=== Lista Final ===\n")
for a in pessoas: 
    a.toString()
print("\n\n")
