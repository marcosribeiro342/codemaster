from funcoes import *
limpa()

pessoas = []

total = int(input("-Quantas pessoas quer registar? "))

print()

for i in range(1, total+1):
    nome = input(f"- Digite o nome da ({i}ª) pessoa: ")
    idade = int(input(f"- Digite a idade da ({i}ª) pessoa: "))
    morada = input(f"- Digite a morada da ({i}ª) pessoa: ")
    pessoas.append(novaPessoa(nome,idade,morada))
    print()



print("="*20)
print()

for i in range(len(pessoas)): toString(i,pessoas[i])
print("\n\n")
