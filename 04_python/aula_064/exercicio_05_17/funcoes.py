import os

#Funções
def mediaDeAprovacao():
    nota_1 = float(input("Qual foi a sua priemira avaliação? "))
    nota_2 = float(input("Qual foi a sua segunda avaliação? "))
    media = (nota_1 + nota_2) / 2
    if media >= (6):
        print(f"Esta APROVADO e a suma média é: ({media:.2f})")
    else:
        print(f"Esta REPROVADO e a sua media é: ({media:.2f})")

   

# Funções Especiais
def limpa():
    if(os.name =="nt"): os.system("cls")
    else:(os.system("clear"))