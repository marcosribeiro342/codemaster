from funcoes import *
from Aluno import *


limpa()

a1 = Aluno("Marcos Ribeiro", 15, "1º Ano A", "Porto")
a2 = Aluno("Rui Sampaio", 16, "2º Ano C", "Braga")
a3 = Aluno("Marcos Ribeiro", 15, "1º Ano A", "Porto")

a1.toString()

print("="*20)

a2.mudar("Vila real")
a1.toString()

print("="*20)

a3.atribuirNotas(14,17)
a3.toString()

print(f"Media do aluno 3: ({a3.getMedia():.1f})")
print("\n\n")
