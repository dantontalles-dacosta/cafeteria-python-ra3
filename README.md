<h1>Documentação do Projeto</h1>
  <p>Glossário geral das funções utilizadas no projeto e suas especificações.</p>


<h2>Funções Específicas</h2>
  <p>Funções que executam funções principais e "macro" no projeto como adicionar itens, finalizar o pedido, etc.</p>
  <br>
  
```
localizarItem()
```

<p>Encontra o item descrito por nome pelo usuário e retorna seu preço e localização no menu.</p>
<br>

```
alterarInfo()
```

<p>Altera as informações contidas no arquivo txt como nome do restaurante e porcentagem do garçom.</p>
<br>

```
finalizarPedido()
```

<p>Permite que o usuário selecione os itens que deseja adicionar ao pedido e finalizar o mesmo, indicando os itens pedidos e o valor total da compra + porcentagem do garçom.</p>
<br>

```
processarPedido()
```

<p>Processa e cruza todos os dados da função finalizarPedido(), retornando as informações e resposta dos cálculos à mesma.</p>
<br>

<h2>Funções Genéricas</h2>
  <p>Funções que não executam funções principais, isto é, mexem com a formatação e manipulação de dados nos arquivos txt e listas, dicionários, matrizes, etc.</p>
  <br>
  
```
lerLinhas(linha, arquivo)
```

<p>Varre a linha indicada pelo parâmetro linha (int) no arquivo indicado pelo parâmetro arquivo (string), retornando uma string com todos o conteúdo da linha.</p>
<br>

```
escreverLinhas(linha, conteúdo, arquivo)
```

<p>Varre a linha indicada pelo parâmetro linha (int) no arquivo indicado pelo parâmetro arquivo (string) e a sobrescreve com o conteúdo indicado pelo parâmetro conteúdo (qualquer formato, a função formata automaticamente para string). A função não retorna nenhum valor.</p>
<br>

```
returnTiposLista(lista)
```

<p>Varre a lista indicada pelo parâmetro lista e retorna todos os tipos/categorias nela incluídos, sem os produtos. Retorna em formato de lista.</p>
<br>

```
returnTiposString(lista)
```
<p>Varre a lista indicada pelo parâmetro lista e retorna todos os tipos/categorias nela incluídos, sem os produtos. Retorna em formato de string e devidamente formatado sem os seguintes caracteres: ",',{,},(,),[,].</p>
<br>

```
returnProdutosLista(tipo, lista)
```
<p>Varre a lista indicada pelo parâmetro lista e retorna todos os produtos do tipo indicado pelo parâmetro tipo (string) nela incluídos. Retorna em formato de lista.</p>
<br>

```
returnProdutosString(tipo, lista)
```
<p>Varre a lista indicada pelo parâmetro lista e retorna todos os produtos do tipo indicado pelo parâmetro tipo (string) nela incluídos. Retorna em formato de string.</p>
<br>

```
returnTiposProdutos(lista)
```

<p>Varre a lista indicada pelo parâmetro lista e retorna todos os tipos e respectivos produtos desses tipos nela incluídos. Retorna em formato de string.</p>
<br>
