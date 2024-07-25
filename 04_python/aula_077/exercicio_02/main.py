from funcoes import *

limpa()

p1 =["fabricio",29,"Porto"]
p2 =["joao",29,"Braga"]
p3 =["Manuel",29,"Coimbra"]



p4 = ["Marcos", 28, 56,1.91, 99.7, 123.4, "Lisboa", 1111123334, 334345566]

p5 = {
    "nome":"marcos",
     'morada': 'porto',
     'idade':30, 
     'saldo': 400
}

p6 = {
    "nome":"marcos",
     'morada': 'porto',
     'idade':30, 
     'saldo': 400,
     "pet":{
         'nome':'rex',
         'peso':7.500,
         'raca': "podle"
     }
}

print(p6['pet']['raca'])

print(p3[1])
print(p5['idade'])

p5['idade'] = 34
print(p5['idade'])


print("\n\n")
