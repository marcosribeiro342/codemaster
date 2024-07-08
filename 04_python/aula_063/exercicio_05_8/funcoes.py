import os

#Funções

def eleitoresDoMunicipio():
    municipio = input("Diga-me o seu municipio: ")
    numero_de_eleitores = int(input("Digite o número de elitores do seu municipio: "))
    votos_brancos = int(input("Digite o número de votos brancos: "))
    votos_nulos = int(input("Digite o número de votos nulos: "))
    votos_validos = int(input("Digite o número de votos validos: "))
    perc_brancos = (votos_brancos / numero_de_eleitores) * 100
    perc_nulos = (votos_nulos / numero_de_eleitores) * 100
    perc_votantes = (votos_validos / numero_de_eleitores) * 100
    print(f"O total de eleitores é ({numero_de_eleitores}), tendo as seguintes percentagens: votos brancos ({perc_brancos} %), votos nulos ({perc_nulos} %) e os votos válido ({perc_votantes} %)  \n")

# Funções Especiais
def limpa():
    if(os.name =="nt"): os.system("cls")
    else:(os.system("clear"))