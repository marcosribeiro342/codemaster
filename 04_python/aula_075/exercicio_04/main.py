from funcoes import *
limpa()

pessoas = []

total = int(input("-Quantas pessoas quer registar? "))

print()

# for i in range(1, total+1):
#     nome_digitado = input(f"- Digite o nome da ({i}ª) pessoa: ")
#     idade_digitada = int(input(f"- Digite a idade da ({i}ª) pessoa: "))
#     morada_digitada = input(f"- Digite a morada da ({i}ª) pessoa: ")
#     nova_pessoa = [nome_digitado,idade_digitada,morada_digitada]
#     pessoas.append(nova_pessoa)
#     print()

for i in range(1, total+1):
    pessoas.append([
        input(f"- Digite o nome da ({i}ª) pessoa: "),
        int(input(f"- Digite a idade da ({i}ª) pessoa: ")),
        input(f"- Digite a morada da ({i}ª) pessoa: ")
    ])
    print()

print("="*20)
print()

for i in range(len(pessoas)):
    print(f"{i+1} - {pessoas[i][0]} (Idade: {pessoas[i][1]}) [Morada:{pessoas[i][2]}]")
print("\n\n")
