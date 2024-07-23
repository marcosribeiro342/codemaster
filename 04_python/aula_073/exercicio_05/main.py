from funcoes import *
import random
limpa()

nomes = ["Marcos", "João","Rui","Paulo","Carina","Maria","Ana","Rita","Carolina","Ines"]
apelidos=["Silva", "Ribeiro", "Oliveira","Barreiro","Pereira"]

aleatorio =random.randint(0,11)

numero_de_nomes = int(input("-Digite o total de nomes completos que voce deseja gerar: "))
animar2("Aguarde")

for i in range(1,numero_de_nomes+1):
  n =random.randint(0,len(nomes)-1)
  a =random.randint(0,len(apelidos)-1)
  print(f"{i}-{nomes[n]} {apelidos[a]}")




print("\n\n")
