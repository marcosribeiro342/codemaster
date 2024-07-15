import funcoes
import math
from funcoes import *
limpa()

numero = int(input("-Digite quantos casos vamos analisar: "))
limpa()
animar("a analisar..")
print()

n = 1
soma_pares = 0
soma_impar = 0
while( n <= numero):
   num= int(input(f"Digite [{n}º] numero: "))
   n += 1
   if num % 2 == 0:
      soma_pares +=1
   
soma_impar = numero - soma_pares
print()

print(f"--- Total de números PARES: ({soma_pares}) ----")
print(f"--- Total de números IMPARES: ({soma_impar}) ----")


   



print("\n\n")
