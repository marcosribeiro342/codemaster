import funcoes
from funcoes import *
limpa()

inicial = int(input("-Digite o valor inicial "))
final = int(input("-Digite o valor final "))

print()
if (inicial < final):
    for i in range(inicial,final+1): print(i)
else:
    for i in range(inicial, final-1,-1):print(i)
    


print("\n\n")
