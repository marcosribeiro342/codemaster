import os
import time

#Funções
def candidaturas(idade, experiencia):
    if idade >= 18 and experiencia.lower() == "sim":
        return "APROVADO PARA ESTÁGIO"
    elif idade >= 18 and experiencia.lower() == "nao":
        return "NÃO APROVADO PARA ESTÁGIO"
    elif idade < 18 and experiencia.lower() == "sim":
        return "APROVADO PARA ESCOLA DE PROGRAMAÇÃO"
    elif idade < 18 and experiencia.lower() == "nao":
        return "NÃO APROVADO PARA ESCOLA DE PROGRAMAÇÃO"
    else:
        return"ERRO NOS DADOS INFORMADOS, TENTE DE NOVO"
    

    
# Funções Especiais
def limpa():
    if(os.name =="nt"): os.system("cls")
    else:(os.system("clear"))
def aguarde(tempo): time.sleep(tempo)