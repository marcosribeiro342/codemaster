import funcoes
import math
from funcoes import *
limpa()

total_alunos = int(input("-Digite o total de alunos da turma: "))

print()

soma_das_idades = 0
for aluno in range(1,total_alunos+1):
    soma_das_idades += int(input(f"-Digite a idade do ({aluno}º) aluno: "))

media = soma_das_idades/ total_alunos

print(f"\n Média: ({media:.1f}) anos")

   



print("\n\n")
