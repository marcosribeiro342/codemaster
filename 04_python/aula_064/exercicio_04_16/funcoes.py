import os

#Funções
def precoMaca():
    maca = int(input("Diga quantas maças quer levar? "))
    if maca < (12):
        print(f"\nO preço total é ({maca * 1.30:.2f})")
    else:
        print(f"\nO preço total é ({maca * 1:.2f})")

   

# Funções Especiais
def limpa():
    if(os.name =="nt"): os.system("cls")
    else:(os.system("clear"))