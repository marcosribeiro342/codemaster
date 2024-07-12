import funcoes
from funcoes import *
limpa()

tabuada = int(input("Qual tabuada quer saber? "))


print(f"=== Tabuada do ( {tabuada} ) ===")

numero = 0
while(numero <= 10):
   print(f"{tabuada} x {numero:>2} = ({tabuada * numero})")
   numero += 1

print("\n\n")
