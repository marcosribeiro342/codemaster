import os
import time
import globais
#Funções


def exibirMenu():
    animar2("Aguarde")
    print("=== Loja ===\n")
    print("1 - Registar produto")
    print("2 - Editar produto")
    print("3 - Apagar produto")
    print("4 - Listar produtos\n")
    print("5 - vendas")
    print("6 - Listar vendas\n")
    print("0 - Sair\n")
    return int(input("-- Opção: "))

#Registar npet
def registarProdutos():
    print("--- Novo produto ---\n")
    nome = input(f"- Digite o nome do novo produto: ")
    if(not nomeJaExiste(nome)):
        preco = float(input(f"- Digite o preço deste produto: "))
        quantidade = int(input(f"- Digite a quantidade deste produto: "))
        globais.produtos.append(novoProduto(nome,preco,quantidade)) 
        print("\n --- Sucesso --")
    else: print("\n--- NOME JÁ EXISTE! ---")
    

#Editar Pet
def editarProdutos():
    print("--- Editar produto ---\n")
    listarProdutos(False)
    id = int(input("\n-Digite o ID do produto que queres editar: ")) -1 
    
    if(id >= 0 and id < len(globais.produtos)):
        print()
        toString(id,globais.produtos[id])
        print()
        

        print("\n--- Editar ---\n")
        print("1 - Nome.")
        print("2 - Preço.")
        print("3 - Quantidade\n")
        print("0 - Cancelar\n")
        opcao = int(input("-- Opção: "))

        print()

        p =globais.produtos[id]
    
        if(opcao ==1):
            nome = input(f"\n- Digite o nome para substituir ({p['nome']}): ")
            if(not nomeJaExiste(nome)):
                p["nome"] =nome
                print("\n--Sucesso--")
            else: print("\n--- NOME JÁ EXISTE! ---")
        elif(opcao == 2):
            p["preco"] = float(input(f"\n- Digite opreço para substituir ({p['preco']:.2f}): "))
            print("\n--Sucesso--")
        elif(opcao == 3):
            p["quantidade"] = float(input(f"\n- Digite a quantidade para substituir ({p['quantidade']}): "))
            print("\n--Sucesso--")
        elif(opcao == 0):
            print("cancelado")
            carrgueEnter()
        else:
            print("--- Operação invalida ---")
    else:
        print("\n--- CÓDIGO INVÁLIDO ---")


#Apagar Produtos
def apagarProduto():
    print("--- Apagar Produto ---\n")
    listarProdutos(False)
    id = int(input("\n-Digite o ID do produto que queres apagar: ")) -1
    if(id >= 0 and id < len(globais.produtos)):
        resposta = input(f"\n- Tem certeza que desesjas apagar o produto ({globais.produtos[id]['nome']}): ")
        if(resposta.lower() == "sim"):
            globais.produtos.pop(id)
            print("\n--- Apagado(a) com sucesso ---")
        else: print("\n--- OPERAÇÃO CANCELADA! ---")
    else:
        print("\n--- CÓDIGO INVÁLIDO ---")

#Listar Produtos
def listarProdutos(com_titulo):
    if(com_titulo):print("--- Lista dos produtos---\n")
    for i in range(len(globais.produtos)): toString(i,globais.produtos[i])

#Vender Produtos
def venderProduto():
    print("--- Vender Produto ---\n")
    listarProdutos(False)
    id = int(input("\n-Digite o ID do produto que queres vender: "))-1
   
    if(id >= 0 and id < len(globais.produtos)):

        p =globais.produtos[id]
        quantidade = int(input(f"\n-Digite a quantidade de ({p['nome']})  que queres vender: "))
        if(quantidade >= 0 and quantidade < (p['quantidade'])):
            nome = p["nome"]
            preco = p["preco"]
            total = preco * quantidade
            globais.vendas.append(novaVenda(nome,preco,quantidade))
            print(f"\nVenda #{len(globais.vendas)} - {p['nome']} ({p['preco']:.2f} * ({quantidade} uni.) = {total})")
            p["quantidade"] -= quantidade
            print("\n---Sucesso---")
        else:print("\n---QUANTIDADE INSUFICIENTE---")
    else:
         print("\n--- CÓDIGO INVÁLIDO ---")

def listarVendas(com_titulo):
    total = 0
    if(com_titulo):print("--- Lista das vendas---\n")
    for i in range(len(globais.vendas)): 
        toString_1(i,globais.vendas[i])
        total += globais.vendas[i]['preco'] * globais.vendas[i]['quantidade']

    print(f"\n O total de vendas: {total}")


#def auxiliares

def novoProduto(nome,preco,quantidade):
    novo_produto = {
        "nome":nome,
        "preco":preco,
        "quantidade":quantidade,
    }
    return novo_produto

def toString(i,produto):
    print(f"#{i+1} (Nome: {produto['nome']}) (preco: {produto['preco']:.2f}) (Quantidade: {produto['quantidade']}) ")

def novaVenda(nome,preco,quantidade):
    venda= {
        "nome":nome,
        "preco":preco,
        "quantidade":quantidade,
    }
    return venda
def toString_1(i,venda):
    print(f"Venda #{i+1} (Nome: {venda['nome']}) (preco: {venda['preco']:.2f}) (Quantidade: {venda['quantidade']}) ")



def init():
    globais.produtos.append(novoProduto("papel", 12.5, 8))
    globais.produtos.append(novoProduto("lapis", 1.5, 8))
    globais.produtos.append(novoProduto("capas", 3.5, 8))
    globais.produtos.append(novoProduto("canetas",2, 8))

def nomeJaExiste(nome):
  for p in globais.produtos:
    if(p["nome"].lowe() == nome.lower()): return True
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