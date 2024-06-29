print("\n\n")

#Váriaveis
teste = "Codemaster"
total_caracter = len(teste)
total_caracter_especifico = teste.count("e")


#Execução
print("String 'original':(" + teste + ")\n" )
print("String 'capitalizada':(" + teste.capitalize() + ")")
print("String 'minúsculas': (" + teste.lower() + ")")
print("String 'maiúsculas':(" + teste.upper() + ")\n")

print("String 'total de letras e':(", total_caracter_especifico, ")", sep="")
print("String 'tamanho total da função':(" , total_caracter , ")\n" , sep="")

print("String 'Substitui todo (e) por (x)':(" + teste.replace("e", "X") +")")

print("\n\n")