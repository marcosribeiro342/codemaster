import os

#Funções
def calculoMedia():
    nota_1 = float(input("Digite a sua primeira nota: "))
    nota_2 = float(input("Digite a sua segunda nota: "))
    nota_3 = float(input("Digite a sua terceira nota: "))
    media = ((nota_1 * 2) + (nota_2 * 3) + (nota_3 * 5)) / 10
    print(f"\nA media final é ( {media:.2f} )")
   

# Funções Especiais
def limpa():
    if(os.name =="nt"): os.system("cls")
    else:(os.system("clear"))