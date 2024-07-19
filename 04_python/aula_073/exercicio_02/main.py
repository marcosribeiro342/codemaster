from funcoes import *
limpa()

lista_1 = ["uva","maçã","morango","ananás","banana","laranja"]
lista_2 = ["bolo","pão","queijo"]

print(lista_1)
print(lista_2)

print()

lista_1.sort()
print(lista_1)

print()

lista_1.sort(reverse=True)
print(lista_1)

print()

if("morango" in lista_1): print("'morango' está na lista 1")
else: print("falso")

print()
print("----------------")
print()

lista_1.extend(lista_2)
print(lista_1)

print()
print("----------------")
print()

lista_1.clear()
print(lista_1)

print("\n\n")
