print("\n\n")

print("=== Media Escolar ===\n")

nome = input( "Digite o nome do aluno: ")
n1 = float(input("-Digite a nota da prova 1: "))
n2 = float(input("-Digite a nota da prova 2: "))
nt = float(input("-Digite a nota do trabalho de casa: "))
media = (n1 + n2 + nt) / 3

print(f"\nO aluno ({nome}) obteve uma média final de ({media:.1f}) valores.")

print("\n\n")