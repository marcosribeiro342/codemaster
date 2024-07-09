import os

#Funções
def numerosCrescentes(x, y):
    if x < y:
        print(f"Os valores crescentes são {x:.0f} e {y:.0f}.")
    else:
        print(f"Os valores crescentes são {y:.0f} e {x:.0f}.")


   

# Funções Especiais
def limpa():
    if(os.name =="nt"): os.system("cls")
    else:(os.system("clear"))