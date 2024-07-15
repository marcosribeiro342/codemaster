import funcoes
from funcoes import *
limpa()

numero = int(input("Digite um numero inteiro: "))

print()

print(f"=== Multiplos de ({numero}) entre 0 e 100 ===")

n = 0
while( n*numero <= 100):
   resultado = n * numero
   n += 1
   print(f"({resultado})")



print("\n\n")
