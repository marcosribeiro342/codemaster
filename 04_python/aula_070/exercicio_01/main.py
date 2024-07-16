import funcoes
from funcoes import *
limpa()

inicial = int(input("-Digite o valor inicial "))
final = int(input("-Digite o valor final "))
repetições = int(input("- Quantas vezes queres que repita? "))

print("="*20)
for rep in range(repetições):
    if (inicial < final):
        for i in range(inicial,final+1): 
            print(i)
    else:
        for i in range(inicial, final-1,-1):print(i)
    print("="*20)


print("\n\n")
