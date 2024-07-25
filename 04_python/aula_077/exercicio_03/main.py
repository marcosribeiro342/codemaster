from funcoes import *

limpa()

p1 = {
    "nome":"Marcos",
    "idade": 30,
    "morada": "Braga"
}

print("=== Dicionário com for ===")

print()

for chave in p1: print(f"{chave} - {p1[chave]}")

print()
print("=== Dicionário apenas as 'chaves' ===")
print()

print(p1.keys())

print()
print("=== Dicionário apenas os 'valores' ===")
print()

print(p1.values())

print("\n\n")
