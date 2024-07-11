import os
import time
import math

#Funções
def areaTriangulo(base, altura):
    resultado = (base * altura) / 2
    return f"A area do seu triangulo é: {resultado:.1f}"

def areaRetangulo(base, altura):
    resultado = (base * altura) 
    return f"A area do seu retângulo é: {resultado:.1f} "

def areaCirculo(raio):
    resultado = math.pi * raio ** 2
    return f"A area do seu circulo é: {resultado:.1f} "
        
    
# Funções Especiais
def limpa():
    if(os.name =="nt"): os.system("cls")
    else:(os.system("clear"))
def aguarde(tempo): time.sleep(tempo)

def animar(frase):
    tempo = 0.3
    limpa()
    print(frase, end="", flush=True)
    aguarde(tempo)
    print(".", end="", flush=True)
    aguarde(tempo)
    print(".", end="", flush=True)
    aguarde(tempo)
    print(".", end="", flush=True)
    limpa()