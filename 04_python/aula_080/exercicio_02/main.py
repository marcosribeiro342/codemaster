from funcoes import *
from Aluno import *
import random


limpa()

alunos = []



alunos.append(Aluno("Marcos Ribeiro", 16, "10º Ano B", "Braga"))
alunos.append(Aluno("Joao Teixeira", 10, "8º Ano B", "Vila Real"))
alunos.append(Aluno("Rita Ferraz", 6, "1º Ano B", "Bragança"))
alunos.append(Aluno("Tomas Oliveira", 8, "3º Ano B", "Viseu"))

for a in alunos:
    n1 = random.randint(0,20) 
    n2 = random.randint(0,20)
    a.atribuirNotas(n1,n2) 

for a in alunos: a.toString()

print("="*20 + "\n")

for i in range(len(alunos)):
    
    alunos[i].toStringID(i)


print("\n\n")
