from funcoes import *
limpa()

frutas = ["uva","maçã","morango","ananás","banana","laranja"]

print("=== Listas de frutas com FOR ===\n")
for f in frutas: print(f)

print("\n=== Listas de frutas com FOR + Range() ===\n")
for i in range(len(frutas)):print(f"{i+1} - {frutas[i]}")

print("\n=== Listas de frutas com FOR + Reverse() ===\n")
for f in reversed(frutas): print(f)

print("\n=== Listas de frutas com FOR + Range Reverse() ===\n")
for i in range(len(frutas)-1,-1,-1): print(f"{i+1} - {frutas[i]}")


print("\n\n")
