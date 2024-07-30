class Pessoa:

    #Constutor
    def __init__(self,nome, idade, morada, nif):
        
        self.nome = nome
        self.idade = idade
        self.morada = morada
        self.nif = nif

    def toString(self):
        print(f"{self.nome:<20}-> (Idade: {self.idade}) (Morada: {self.morada}) (NIF:{self.nif})")
        
    def completarAnos(self):
        self.idade += 1
        print(f"{self.nome} fez anos!!")

    def mudar(self,nova_morada):
        print(f"{self.nome} modou-se de ({self.morada:<10} -> {nova_morada:>10})")
        self.morada = nova_morada
    
    
    