import os

#Funções
def numerosCrescentes(x, y):
    if x < y:
        print(f"Os valores crecentes são {x:.0f} e {y:.0f}.")
    elif y < x:
        print(f"Os valores crecentes são {y:.0f} e {x:.0f}.")
    else:
        print("Entrada Invalida")

   

# Funções Especiais
def limpa():
    if(os.name =="nt"): os.system("cls")
    else:(os.system("clear"))