linhaPrincipais = 0
linhaSobremesas = 1
linhaEntradas = 2
linhaBebidas = 3
pedidoValores = 0
pedidoProdutos = ""

## loop inicial & inicialização de valores.

def escritaInicial():
    """Faz a escrita inicial dos dados no arquivo txt."""
    initLista = ['[{"sanduíches":{"x-tudo":"20", "baurú":"15"}},{"salgados":{"coxinha":"7", "bolinho de carne":"6"}}]',
                 '[{"sorvete":{"sorvete de morango":"6", "sorvete de chocolate":"6"}},{"bolos":{"bolo de chocolate (fatia)":"5", "bolo de milho (fatia)":"5"}}]',
                 '[{"pão de queijo":{"pão de queijo comum (5 unidades)":"4", "pão de queijo recheado (2 unidades)":"3"}}]',
                 '[{"refrigerantes":{"coca-cola":"8", "sprite":"7"}},{"sucos":{"suco de manga":"8", "suco de uva":"9"}}]']

    initInfo = ['{"nome":"Molejo"}','{"porcentagem":"8"}']

    with open("menu.txt", "w", encoding="utf-8") as file:
        for i in range(4):
            if i < 3:
                file.writelines(f"{initLista[i]}\n")
            else:
                file.writelines(f"{initLista[i]}")

    with open("info.txt", "w", encoding="utf-8") as file:
        for i in range(0,2):
            if i < 1:
                file.writelines(f"{initInfo[i]}\n")
            else:
                file.writelines(f"{initInfo[i]}")

def menuPrincipal():

    pedidoValores = 0
    pedidoProdutos = ""

    ## pegar o nome da cafeteria do arquivo
    linha = lerLinhas(0, "info.txt")
    dicTemp = eval(linha)
    for i in dicTemp:
        nome = dicTemp[i]

    print(f"\n\n\n\n\n\n\n\n\n---------------------------------------\n\nEsse é o cardápio eletrônico da cafeteria {nome}!\nAs funções disponíveis são as seguintes: \n\n[1] Adicionar um item ao menu\n[2] Subtrair um item do menu\n[3] Alterar um item do menu\n[4] Buscar itens no menu\n[5] Listar o menu\n[6] Fazer um pedido (com cálculo de valor incluso!)\n[7] Alterar o nome do restaurante/porcentagem do garçom\n[0] Encerrar o programa\n\n---------------------------------------")

    varEscolher = int(input("\nSua escolha: "))

    if varEscolher == 1:
        adicionarItem()
    elif varEscolher == 2:
        subtrairItem()
    elif varEscolher == 3:
        alterarItem()
    elif varEscolher == 4:
        localizarItem()
    elif varEscolher == 5:
        listarMenu()
    elif varEscolher == 6:
        finalizarPedido(pedidoValores, pedidoProdutos)
    elif varEscolher == 7:
        alterarInfo()

## funções básicas do programa.
#Luan (A de remover pode reutilizar bastante do adicionar)
def adicionarItem():
    while True:
        # Ler o menu a partir do arquivo "menu.txt"
        linhas = [lerLinhas(i, "menu.txt") for i in range(4)]
        dic_menu = [eval(linha) for linha in linhas]

        # Exibir categorias numeradas
        print("\nSelecione uma categoria para adicionar um item:")
        categorias = []
        for linha in dic_menu:
            for categoria_dict in linha:
                for categoria in categoria_dict.keys():
                    categorias.append(categoria)
        
        for i, categoria in enumerate(categorias, 1):
            print(f"[{i}] {categoria}")

        # Receber a categoria selecionada pelo usuário
        categoria_escolhida = int(input("\nEscolha o número da categoria: ")) - 1

        # Validar a entrada do usuário
        if 0 <= categoria_escolhida < len(categorias):
            categoria_nome = categorias[categoria_escolhida]

            # Receber o nome e custo do novo produto
            nome_produto = input(f"\nDigite o nome do novo produto para {categoria_nome}: ")
            custo_produto = int(input("Digite o custo do novo produto (em inteiro): "))

            # Encontrar a linha correspondente e adicionar o produto
            linha_categoria = categoria_escolhida // 2
            linha_dic = dic_menu[linha_categoria]
            
            # Adicionar o novo produto ao dicionário da categoria correta
            for subcategoria_dict in linha_dic:
                if categoria_nome in subcategoria_dict:
                    subcategoria_dict[categoria_nome][nome_produto] = str(custo_produto)

            # Escrever a linha atualizada de volta ao arquivo
            escreverLinhas(linha_categoria, str(linha_dic), "menu.txt")
            print(f"\nProduto '{nome_produto}' adicionado com sucesso à categoria '{categoria_nome}'.")

            # Perguntar se o usuário quer adicionar outro produto
            continuar = input("\nDeseja adicionar outro produto? (s/n): ")
            if continuar.lower() != 's':
                break
        else:
            print("\nEscolha inválida. Tente novamente.")

    menuPrincipal()

def subtrairItem():
        while True:
            # Ler o menu a partir do arquivo "menu.txt"
            linhas = [lerLinhas(i, "menu.txt") for i in range(4)]
            dic_menu = [eval(linha) for linha in linhas]

            # Exibir categorias numeradas
            print("\nSelecione uma categoria para excluir um item:")
            categorias = []
            for linha in dic_menu:
                for categoria_dict in linha:
                    for categoria in categoria_dict.keys():
                        categorias.append(categoria)

            for i, categoria in enumerate(categorias, 1):
                print(f"[{i}] {categoria}")

            # Receber a categoria selecionada pelo usuário
            categoria_escolhida = int(input("\nEscolha o número da categoria: ")) - 1

            # Validar a entrada do usuário
            if 0 <= categoria_escolhida < len(categorias):
                categoria_nome = categorias[categoria_escolhida]

                # Exibir os produtos da categoria escolhida
                produtos = dic_menu[categoria_escolhida // 2][categoria_nome]
                print(f"\nProdutos disponíveis em '{categoria_nome}':")
                for produto, custo in produtos.items():
                    print(f"{produto}: {custo}")

                # Receber o nome do produto a ser excluído
                produto_excluir = input(f"\nDigite o nome do produto a ser excluído de '{categoria_nome}': ")

                # Verificar se o produto existe na categoria
                if produto_excluir in produtos:
                    # Remover o produto do dicionário da categoria correta
                    del dic_menu[categoria_escolhida // 2][categoria_nome][produto_excluir]

                    # Escrever a linha atualizada de volta ao arquivo
                    escreverLinhas(categoria_escolhida // 2, str(dic_menu[categoria_escolhida // 2]), "menu.txt")
                    print(f"\nProduto '{produto_excluir}' removido com sucesso da categoria '{categoria_nome}'.")

                    # Perguntar se o usuário deseja excluir outro produto
                    continuar = input("\nDeseja excluir outro produto? (s/n): ")
                    if continuar.lower() != 's':
                        break
                else:
                    print(f"\nProduto '{produto_excluir}' não encontrado em '{categoria_nome}'. Tente novamente.")
            else:
                print("\nEscolha inválida. Tente novamente.")

    menuPrincipal()

def alterarItem():
    menuPrincipal()

def localizarItem():
    print("\n---------------------------------------\n\nQual o nome do item que você deseja localizar?\n\n---------------------------------------\n")

    varAchou = False

    nomeItem = input("")
    linha1 = lerLinhas(0,"menu.txt")
    linha2 = lerLinhas(1,"menu.txt")
    linha3 = lerLinhas(2,"menu.txt")
    linha4 = lerLinhas(3,"menu.txt")

    dic1 = eval(linha1)
    dic2 = eval(linha2)
    dic3 = eval(linha3)
    dic4 = eval(linha4)

    listAll = []

    for i in range(1,5,1):
        listAll.append(eval(f"dic{i}"))

    for i in listAll:
        for x in i:
            for y, z in x.items():
                for j, k in z.items():
                    if str(j) == nomeItem.lower():
                        print(f"\n---------------------------------------\n\nO item {nomeItem} tem preço R${k} e se encontra na categoria {y}.\n\n[1] Procurar outro item\n\n[2] Voltar ao menu principal\n\n---------------------------------------\n\n")
                        varChoose = int(input(""))
                        varAchou = True
                        if varChoose == 1: 
                            localizarItem()
                        else:
                            menuPrincipal()
                    else:
                        varAchou = False

    if varAchou == False:
        print("\n\nO item não foi encontrado na nossa base de dados. Tem certeza de que digitou corretamente ou lembrou de cadastrá-lo?\n\n[1] Procurar novamente\n[2] Voltar ao menu principal")
        chooseVar = int(input("\n\n"))

        if chooseVar == 1:
            localizarItem()
        else:
            menuPrincipal()

def listarMenu():
    menuPrincipal()

def finalizarPedido(pedidoValores, pedidoProdutos):
    """Faz a simulação de preço do pedido do cliente, detalhando o valor pós-calculo de porcentagem do garçom e os itens comprados."""
    linha = lerLinhas(1, "info.txt")
    dicTemp = eval(linha)
    for i in dicTemp:
        por = int(dicTemp[i])

    print("------------------------------- \n\nOk, vamos fazer o pedido! :) \nQual a categoria do item?\n\n[1] Pratos principais\n[2] Sobremesas\n[3] Entradas\n[4] Bebidas \n[5] Finalizar o pedido\n[0] Voltar ao menu principal\n\n-------------------------------\n\n ")

    varEscolher = int(input(""))

    if varEscolher == 1:
        pedidoValores, pedidoProdutos = processarPedido(linhaPrincipais, pedidoValores, pedidoProdutos)
        finalizarPedido(pedidoValores, pedidoProdutos)  

    elif varEscolher == 2:
        pedidoValores, pedidoProdutos = processarPedido(linhaSobremesas, pedidoValores, pedidoProdutos)
        finalizarPedido(pedidoValores, pedidoProdutos) 

    elif varEscolher == 3:
        pedidoValores, pedidoProdutos = processarPedido(linhaEntradas, pedidoValores, pedidoProdutos)
        finalizarPedido(pedidoValores, pedidoProdutos) 

    elif varEscolher == 4:
        pedidoValores, pedidoProdutos = processarPedido(linhaBebidas, pedidoValores, pedidoProdutos)
        finalizarPedido(pedidoValores, pedidoProdutos) 

    elif varEscolher == 5:
        print(f"\n\n-------------------------------\n\nO valor do seu pedido (+ a taxa do garçom) deu R${pedidoValores + (pedidoValores * (por / 100))} e os itens pedidos foram os seguintes: {pedidoProdutos}.\n\n-------------------------------\n\n")
        menuPrincipal()

    else:
        menuPrincipal()    

def processarPedido(linhaMenu, pedidoValores, pedidoProdutos):
        
        linha = lerLinhas(linhaMenu, "menu.txt")
        dicTemp = eval(linha)
        tipos = returnTiposString(dicTemp)
        print(f"\n-------------------------------\n\nNessa categoria, temos os itens: \n\n{tipos}\n\nEm qual desses itens está o produto que você quer?\n\n-------------------------------\n\n")
        varItem = int(input("(use a posição do item para pedir. ex: [1] Primeiro item, [2] Segundo item, etc): "))

        produtos = returnProdutosString(varItem, dicTemp)
        print(f"\n-------------------------------\n\nNesse item, temos os produtos: {produtos} \n\nQual deles você quer?\n\n-------------------------------\n\n")
        varPedido = int(input("(use a posição do item para pedir. ex: [1] Primeiro item, [2] Segundo item, etc): "))

        contadorProd = 0
        contadorTipo = 0
        for item in dicTemp:
            for label, value in item.items():
                contadorTipo += 1
                if contadorTipo == varItem:
                    for produto, valor in value.items():
                        contadorProd += 1
                        if contadorProd == varPedido:
                            pedidoValores += int(valor)
                            pedidoProdutos += f"\n{produto}"
        
        return pedidoValores, pedidoProdutos

def alterarInfo():
    """Altera as informações contidas no arquivo 'info.txt'."""

    print("\n-------------------------------\n\nOk, colaborador! Que informações você quer alterar?\n\n[1] Nome do restaurante\n[2] Porcentagem do garçom\n\n-------------------------------")

    varEscolha = int(input("\n"))

    if varEscolha == 1:
        linha = lerLinhas(0, "info.txt")
        dicTemp = eval(linha)

        for i in dicTemp:
            nomeAntigo = dicTemp[i]

        nome = input(f"\n-------------------------------\n\nE qual deve ser o novo nome do restaurante? O atual é {nomeAntigo}. \n\nATENÇÃO: essa é uma escolha muito importante, consulte seus superiores primeiro antes de fazer alterações no nome do restaurante, afinal, o marketing é a alma do negócio!\n\nNovo nome: ")

        for i in dicTemp:
            dicTemp[i] = nome

        escreverLinhas(1, dicTemp, "info.txt")
        print(f"\n\nNome alterado com sucesso! A cafeteria agora se chama {nome}.\n\n")
        menuPrincipal()
    elif varEscolha == 2:
        linha = lerLinhas(1, "info.txt")
        dicTemp = eval(linha)

        for i in dicTemp:
            porAntiga = dicTemp[i]

        por = input(f"E qual deve ser a nova porcentagem do garçom? A atual é {porAntiga}. \n\nATENÇÃO: o garçom vai ficar extremamente chateado se você mexer com a porcentagem dele, esteja avisado!\n\nNova porcentagem: ")

        for i in dicTemp:
            dicTemp[i] = por

        escreverLinhas(2, dicTemp, "info.txt")
        menuPrincipal()
    else:
        menuPrincipal()

## funções genéricas p/auxiliar na manipulação de dados.

def lerLinhas(linha, arquivo):
    """Retorna a linha inteira no arquivo indicado como uma string. \n\nExige os parâmetros linha a ser copiada (int) e arquivo a ser lido (string). \n\nex: Preciso ler a linha 8 do arquivo receitas, lerLinhas(8, 'receitas.txt')."""

    with open(f"{arquivo}", "r", encoding="utf-8") as file:
        content = file.readlines()
        return content[linha]
    
def escreverLinhas(linha, conteudo, arquivo):
    """Sobrescreve a linha do arquivo indicado com o conteúdo fornecido. Não retorna nada.\n\nExige os parâmetros linha a ser sobrescrita (int), conteúdo (qualquer um, pois a função formata para string) e arquivo (string)."""

    with open(f"{arquivo}",'r', encoding="utf-8") as f:
        get_all = f.readlines()

    with open(f"{arquivo}", "w") as file:
        for i,line in enumerate(get_all,1):
            if i == linha:
                file.writelines(f"{conteudo} \n")
            else:
                file.writelines(line)

def returnTiposLista(lista):
    """Dada uma lista, retorna todos os tipos de itens contidos nela como uma lista.\n\nExige como parâmetro uma lista.\n\nNão confundir tipo com categoria: 'bebida' é categoria, 'suco' é tipo."""

    tipos = []

    for item in lista:
        for label, produto in item.items():
            tipos.append(f"{label}")

    return tipos

def returnTiposString(lista):
    """Dada uma lista, retorna todos os tipos de itens contidos nela como uma string.\n\nExige como parâmetro uma lista.\n\nNão confundir tipo com categoria: 'bebida' é categoria, 'suco' é tipo."""

    tipos = []

    for item in lista:
        for label, produto in item.items():
            tipos.append(f"{label}")

    return str(tipos).replace("[","").replace("]","").replace("'","").replace('"',"")

def returnProdutosLista(tipo, lista):
    """Dado um tipo e uma lista, retorna todos os produtos contidos naquele tipo como uma lista.\n\nExige como parâmetro tipo (string) e lista.\n\n"""
    produtos = []
    contador = 0
    for item in lista:
        for label, value in item.items():
            contador +=1
            if contador == tipo:
                for produto, valor in value.items():
                    produtos.append(f"{produto}: {valor}")
    return produtos

def returnProdutosString(tipo, lista):
    """Dado um tipo e uma lista, retorna todos os produtos contidos naquele tipo como uma string.\n\nExige como parâmetro tipo (string) e lista.\n\n"""
    produtos = ""
    contador = 0
    for item in lista:
        for label, value in item.items():
            contador +=1
            if contador == tipo:
                for produto, valor in value.items():
                    produtos += f"\n\n{produto}: {valor} reais"
    return str(produtos)

def returnTiposProdutos(lista):
    """Dada uma lista, retorna todos os tipos de itens contidos nela e os produtos contidos nesses tipos.\n\nExige como parâmetro uma lista.\n\nNão confundir tipo com categoria: 'bebida' é categoria, 'suco' é tipo/item e 'suco de goiaba' é produto."""

    tipos = []

    for item in lista:
        for label, produto in item.items():
            tipos.append(f"{label}:{produto}")

    strTipos = str(tipos)

    return strTipos.replace("{","").replace("}","").replace("[","").replace("]","").replace('"',"").replace("'","")


## inicialização do programa.

escritaInicial()
menuPrincipal()