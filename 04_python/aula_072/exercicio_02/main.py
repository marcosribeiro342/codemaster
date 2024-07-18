import funcoes
from funcoes import *
limpa()

lista_original =["uva", "maca","morango","ananás", "banana", "laranja"]
print(lista_original)
print(f"O primeiro elemento é: {lista_original[0]}")
print(f"O ultimo elemento é: {lista_original[len(lista_original)-1]}")
print(f"O ultimo elemento é: {lista_original[-1]}")
print(f"A sublista contendo do 2º até ao 4º elemento {lista_original[1:4]}")
lista_original[1] ="clementina"
print(f"{lista_original}")



print("\n\n")
