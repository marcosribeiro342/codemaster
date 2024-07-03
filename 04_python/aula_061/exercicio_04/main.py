print("\n\n")
print("{:=^20}".format("Inicio") + "\n")

chuva = input("Esta a chover? ")

print()

if(chuva.lower() == "sim"):

    sair = input("Queres sair de casa? ")

    print()

    if(sair.lower() == "sim"): 
        print("vamos ao cinema")
    else: 
        print("vamos pedir um Glovo") 

else:
    print("Vamos ao parque")

print("\n" + "{:=^20}".format("Fim"))
print("\n\n")