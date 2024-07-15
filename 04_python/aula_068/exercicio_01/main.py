import funcoes
from funcoes import *
limpa()

numero = int(input("Digite um numero inteiro: "))

print()

print(f"=== Multiplos de ({numero}) entre 0 e 100 ===")

n = 0
while( n <= 100):
   print(f"({n})")
   resultado = n * numero
   n += numero
   



print("\n\n")
