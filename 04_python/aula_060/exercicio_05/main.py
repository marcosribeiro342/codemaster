print("\n\n")

resposta = "sim"
saldo = 10

condicao_1 = (resposta.lower() == "sim" or resposta.lower() == "s")

condicao_2 = (resposta.lower() == "sim" or saldo >= 20)

condicao_3 = (resposta.lower() == "sim" and saldo >= 20)

condicao_4 = (not saldo > 20)

condicao_5 = ((resposta.lower() == "sim" or saldo >= 20) and saldo >= 20)

print(f"condicao_1: ({condicao_1})")
print(f"condicao_2: ({condicao_2})")
print(f"condicao_3: ({condicao_3})")
print(f"condicao_4: ({condicao_4})")
print(f"condicao_5: ({condicao_5})")
# print(f"condicao_6: ({condicao_6})")



print("\n\n")