import funcoes
import math
from funcoes import *
limpa()

numero = int(input("-Digite quantos casos vamos analisar: "))
limpa()
animar("a analisar..")
print()

n = 1
while( n <= numero):
   num= int(input(f"Digite [{n}º] numero: "))
   if n == 1:
      menor = num
      maior = num
   else:  
      if num > maior:
         maior = num
      if menor > num:
         menor = num
   n += 1


print()

print(f"--- O número maior é: ({maior}) ----")
print(f"--- O número menor é: ({menor}) ----")


   



print("\n\n")
