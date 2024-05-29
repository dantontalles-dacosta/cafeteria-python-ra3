linhaPrincipais = 1
linhaSobremesas = 2
linhaEntradas = 3
linhaBebidas = 4

def menuPrincipal():

    print("---------------------------------------\n\nSeja bem vindo(a) a nossa cafeteria! O que deseja pra hoje? :) \n\nDigite 1 para adicionar um item ao menu, digite 2 para subtrair um item do menu, digite 3 para alterar um item do menu, digite 4 para buscar itens no menu, digite 5 para listar o menu, digite 6 para fazer um pedido (com cálculo de valor incluso!) ou digite 0 para encerrar esse atendimento.\n\n---------------------------------------")

    varEscolher = int(input("\nSua escolha: "))

    if varEscolher == 1:
        addItem()
    elif varEscolher == 2:
        subItem()
    elif varEscolher == 3:
        altItem()
    elif varEscolher == 4:
        locItem()
    elif varEscolher == 5:
        listMenu()
    elif varEscolher == 6:
        finPedido()


def addItem():
    categoriaItem = int(input("Qual categoria de produto você deseja? 0 para pratos principais, 1 para sobremesas, 2 para entradas e 3 para bebidas: "))
    categoria = lerLinhas(categoriaItem)
    print(escreverLinhas(2,5))

def subItem():
    print()

def altItem():
    print()

def locItem():
    print()

def listMenu():
    print()

def finPedido():
    print()

def lerLinhas(linha):
    """Recebe um valor inteiro correspondente à linha desejada no arquivo txt e retorna o conteúdo da respectiva."""

    with open("menu.txt", "r") as file:
        content = file.readlines()
        return content[linha]
    
def escreverLinhas(linha, conteudo):
    """Recebe um valor inteiro correspondente à linha desejada no arquivo txt e o conteúdo para substituição, subscrevendo o conteúdo da respectiva. A função não retorna valor algum. A ordem de parâmetros é primeiro linha e depois conteúdo."""

    with open("menu.txt",'r') as f:
        get_all = f.readlines()

    with open("menu.txt", "w") as file:
        for i,line in enumerate(get_all,1):
            if i == linha:
                file.writelines(f"{conteudo} \n")
            else:
                file.writelines(line)

menuPrincipal()