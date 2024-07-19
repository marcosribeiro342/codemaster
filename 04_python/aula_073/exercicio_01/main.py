from funcoes import *
limpa()

lista_1 = ["cadeira","mesa","bola","x-acto","caneta"]
lista_2 = ["laranja","morango","ananás"]

print(lista_1)
lista_1.sort()
print(lista_1)

lista_1.sort(reverse=True)
print(lista_1)


if("morango" in lista_2): print("Verdadeiro")
else: print("falso")

lista_1.extend(lista_2)
print(lista_1)

lista_1 = []
lista_1.clear()
print(lista_1)

print("\n\n")
