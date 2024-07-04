print("\n\n")
print("{:=^20}".format("Inicio") + "\n")

def grausKelvin(c):
    k = c + 273.15
    print(f"--- ({c:.2f} c) = ( {k:.2f} k) --- \n")

def grausFahrenheit(c):
    f = c * 1.8 + 32
    print(f"--- ({c:.2f} c) = ( {f:.2f} f) --- \n")

c = float(input("Digite uma temperatura em celsius: "))

print()

graus = input("Voce deseja converter para (k)elvin ou (F)ahrenheit? ")

if (graus.lower() == "k"):
    grausKelvin(c)
elif( graus.lower() == "f"):
    grausFahrenheit(c)
else:
    print("opção inválida")
                

print("\n" + "{:=^20}".format("Fim"))
print("\n\n")