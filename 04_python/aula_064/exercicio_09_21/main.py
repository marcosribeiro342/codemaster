import funcoes
from funcoes import *

limpa()

hora_inicio = int(input("Diga a que horas começou o jogo: "))
hora_fim = int(input("Diga a que horas acabou o jogo: "))

duracao(hora_inicio, hora_fim)


print("\n" + "{:=^20}".format("Fim"))
print("\n\n")
