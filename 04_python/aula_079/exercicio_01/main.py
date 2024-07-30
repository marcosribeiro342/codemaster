from funcoes import *
from Pessoa import *


limpa()

p1 = Pessoa("Marcos", 28, "Trandeiras")


print(p1.nome)
print(p1.idade)
print(p1.morada)

p1.idade += 1

print("="*20)

# print(f"{p1.nome} - (Idade: {p1.idade}) [Morada: {p1.morada}]")
p1.toString()


print("\n\n")
