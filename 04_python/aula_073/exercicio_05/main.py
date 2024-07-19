from funcoes import *
limpa()

nome_dos_alunos = []
numero_de_alunos = int(input("-Quantos alunos serão Registados: "))
animar2("Aguarde")

for i in range(numero_de_alunos):
    nome_dos_alunos.append(input(f"-Diga o nome do(a) [{i+1}]º aluno(a): "))

animar2("Aguarde")
nome_dos_alunos.sort()
print("=== Lista de Alunos Ordenada ===\n")
for i in range(len(nome_dos_alunos)):print(f"{i+1} - {nome_dos_alunos[i]}")


print("\n\n")
