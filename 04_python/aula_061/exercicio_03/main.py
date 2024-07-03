print("\n\n")
print("{:=^20}".format("Inicio") + "\n")

temp = float(input("-Qual a temperatura atual? "))

print()

if(temp <= 18):
    print("Use roupas grossas e casaco")

elif(temp < 28):
    print("Use roupas normais")

else:
    print("use roupas leves")

print()

chuva = input("-Esta a chover? ")

print()

if(chuva.lower() == "sim"):  
    print("Busca o guarda chuva")

print("Vamos passear")


print("\n" + "{:=^20}".format("Fim"))
print("\n\n")