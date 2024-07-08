import os

#Funções
def duracao(hora_de_inicio, hora_de_fim):
    duracao_do_jogo = hora_de_fim - hora_de_inicio
    
    if hora_de_inicio > 24:
        print("O dia só tem 24 horas.")
    elif hora_de_fim > 24:
        print("O dia só tem 24 horas.") 
    elif hora_de_inicio > hora_de_fim:
        print(f"A duração do jogo foi {duracao_do_jogo + 24} horas")
    else:
        print(f"A duração do jogo foi {duracao_do_jogo} horas")

    
# Funções Especiais
def limpa():
    if(os.name =="nt"): os.system("cls")
    else:(os.system("clear"))