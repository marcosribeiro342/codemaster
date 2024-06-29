#importações
import math
import random

print("\n\n")

#Variaveis
inteiro_original = -10
float_original = 3.567


#Executar
print("=== Funções dos Inteiros ===")
print("Inteiro 'original': (" , inteiro_original , ")" , sep="")
print("Inteiro 'original': (" , abs(inteiro_original) , ")\n" , sep="")

print("Número inteiro aleatório 'entre 1 e 5': (" , random.randint(1,5) , ")\n" , sep="")


print("=== Funções dos floats === \n")

print("Float 'original':(" , float_original , ")\n", sep="")

print("Float 'arredondado':(",round(float_original), ")" , sep="")
print("Float 'arredondado para 1 casa decimal':(",round(float_original , 1), ")" , sep="")
print("Float 'arredondado para 1 casa decimal':(",round(float_original , 2), ")\n" , sep="")

print("Float 'arredondado para cima': (", math.ceil(float_original) , ")" , sep="")
print("Float 'arredondado para baixo': (", math.floor(float_original) , ")" , sep="")


print("\n\n")