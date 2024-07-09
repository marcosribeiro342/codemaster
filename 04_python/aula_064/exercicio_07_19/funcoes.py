import os

#Funções
def verificarNumeros(x, y):
    if x > y:
        print(f"O valor ({x}) é o maior.")
    else:
        print(f"O valor ({y}) é o maior.")
    

   

# Funções Especiais
def limpa():
    if(os.name =="nt"): os.system("cls")
    else:(os.system("clear"))