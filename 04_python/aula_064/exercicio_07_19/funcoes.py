import os

#Funções
def numerosCrescentes(x, y):
    if x > y:
        print(f"O valor ({x}) é o maior.")
    elif y > x:
        print(f"O valor ({y}) é o maior.")
    else:
        print("Entrada Invalida")

   

# Funções Especiais
def limpa():
    if(os.name =="nt"): os.system("cls")
    else:(os.system("clear"))