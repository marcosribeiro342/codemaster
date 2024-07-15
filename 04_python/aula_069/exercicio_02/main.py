import funcoes
import math
from funcoes import *
limpa()

tabuada = int(input("-Digite a tabuada que quer saber: "))

print()

for i in range(11): print(f"{i:>2} x {tabuada} = {i * tabuada}")
print()
for i in range(10): print(i + 1)

print()
for i in range(1,11): print(i)

print()
for i in range(0,101,7): print(i)

print()
for i in range(0,101,tabuada): print(i)

print()
for i in range(10, 0, -1): print(i)

print("\n\n")
