#importações
import math
import random

print("\n\n")

#Variaveis
nome = "Marcos"
apelido = "Ribeiro"
idade = "34"
morada = "Vila Pouca de Aguiar"

#Executar
print("Sou o ", nome, " ", apelido, ", tenho ", idade, " anos, e moro na ",morada, ".", sep="")

print(f"sou o {nome} {apelido}, tenho {idade} anos, e moro na {morada}.")

print("sou o {} {}, tenho {} anos, e moro na {}.".format(nome, apelido, idade, morada))


#Em programação os index começam-se a contar desde o "0"
print("sou o {0} {1}, tenho {2} anos, e moro na {3}.".format(nome, apelido, idade, morada))


print("\n\n")