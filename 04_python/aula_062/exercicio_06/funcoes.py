import os

#funções 
def grausKelvin(c):
    k = c + 273.15
    print(f"--- ({c:.2f} c) = ( {k:.2f} k) --- \n")

def grausFahrenheit(c):
    f = c * 1.8 + 32
    print(f"--- ({c:.2f} c) = ( {f:.2f} f) --- \n")

#funções especiais
def limpa():
    if(os.name =="nt"): os.system("cls")
    else:(os.system("clear"))