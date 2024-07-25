import os
import time
#Funções

def novaPessoa(nome, cargo, salario):
    pessoa_individual =[nome,cargo,salario]
    return pessoa_individual

def exibirMenu():
    animar2("Aguarde")
    print("=== Cadastro de Colaboradores ===\n")
    print("1 - Novo colaborador.")
    print("2 - Editar colaborador.")
    print("3 - Apagar colaborador\n")
    print("4 - Listar todos os Colaboradores\n")
    print("0 - Sair\n")
    return int(input("-- Opção: "))

#Registar novo colaborador
def registarColaborador():
    print("--- Novo Colaborador ---\n")
    nome = input(f"- Digite o Nome do novo colaborador: ")
    if(not nomeJaExiste(nome)):
        cargo = input(f"- Digite o cargo do novo colaborador: ")
        salario = float(input(f"- Digite o salário do novo colaborador "))
        globais.colaboradores.append(novaPessoa(nome,cargo,salario)) 
        print("\n --- Sucesso --")
    else: print("Nome já existe")

#Editar novo colaborador
def editarColaborador():
    print("--- Edição de colaborador ---\n")
    listarColaboradores(False)
    id = int(input("\n-Digite o ID do colaborador que queres editar: ")) 
    if(id >= 0 and id < len(globais.colaboradores)):

        opcao_2=editarPormenorizado()
        
        if(opcao_2 ==1):editarNome(id)
        elif(opcao_2 == 2):editarCargo(id)
        elif(opcao_2 == 3):editarSalario(id)
        elif(opcao_2 ==0):
            print("Cancelar")
            carrgueEnter()
        else:
            print("--- Dados Inválidos ---")
    else:
        print("\n--- CÓDIGO INVÁLIDO ---")


#Apagar colaborador
def apagarColaborador():
    print("--- Apagar Pessoa ---\n")
    listarColaboradores(False)
    id = int(input("\n-Digite o ID da pessoa que queres apagar: ")) 
    if(id >= 0 and id < len(globais.colaboradores)):
        apagar = globais.colaboradores.pop(id)
        print(f"\n---({apagar[0]}) Apagado(a) com sucesso ---")
        
    else:
        print("\n--- CÓDIGO INVÁLIDO ---")

#Listar colaboradores
def listarColaboradores(com_titulo):
    if(com_titulo):print("--- Lista das pessoas ---\n")
    ordenado = 0
    for i in range(len(globais.colaboradores)): toString(i,globais.colaboradores[i])
    if(com_titulo):ordenado += globais.colaboradores[i][2]
    
    print()

    if(com_titulo):
        print(f"Total de colaboradores: {len(globais.colaboradores)}.")
        print(f"Total de salarios da empresa: {ordenado:.2f}")
     

def toString(i,pessoa_individual):
    print(f"(ID: {i} ) | ({pessoa_individual[0]}) | (Cargo: {pessoa_individual[1]}) | (Salário:{pessoa_individual[2]:.2f}€)")
    
def editarPormenorizado():
    print("\n--- Editar ---\n")
    print("1 - Nome.")
    print("2 - Cargo.")
    print("3 - Salario\n")
    print("0 - Cancelar\n")
    return int(input("-- Opção: "))

def editarNome(id):
        novo_nome = input(f"\n-Digite nome para substituir ({globais.colaboradores[id][0]}): ")
        if(not nomeJaExiste(novo_nome)):
            globais.colaboradores[id][0] = novo_nome
            print("\n--- Sucesso ---")
        else:print("Nome ja existe")

def editarCargo(id):
        novo_cargo = input(f"\n-Digite o novo Cargo para substituir ({globais.colaboradores[id][1]}): ")
        globais.colaboradores[id][1] = novo_cargo
        print("\n--- Sucesso ---")

def editarSalario(id):
        novo_salario = float(input(f"\n-Digite o novo salario para substituir ({globais.colaboradores[id][2]}): "))
        globais.colaboradores[id][2] = novo_salario
        print("\n--- Sucesso ---")



#def auxiliares

def nomeJaExiste(nome):
    for c in globais.colaboradores:
        if(c[0] == nome):True
    return False


# Funções Especiais
def limpa():
    if(os.name =="nt"): os.system("cls")
    else:(os.system("clear"))
def aguarde(tempo): time.sleep(tempo)

def animar(frase):
    tempo = 0.3
    limpa()

    print(frase, end="", flush=True)
    for i in range(3):
        print(".", end="", flush=True)
        aguarde(tempo)
    
    limpa()

def animar2(frase):
    tempo =0.1
    limpa()
    frase += "..."

    for letra in frase:
        print(letra, end="", flush=True)
        aguarde(tempo)
    limpa()

def animar3(frase):
    tempo =0.1
    limpa()

    for letra in frase:
        print(letra, end="", flush=True)
        aguarde(tempo)
    
    for i in range (3):
        print(".", end="", flush=True )
        aguarde(0.5)

def carrgueEnter():
    input('\nPressione ENTER para continuar...')