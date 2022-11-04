preco_produtos = [100, 150, 300, 5500]
produtos = ['vinho', 'cafeteira', 'microondas', 'iphone']

impostos = []
for item in preco_produtos:
  impostos.append(item * 0.3)


##List Comprehensions
impostos = [preco * 0.3 for preco in preco_produtos]


#Function + List Comprehensions
def calcular_imposto(preco, imposto):
  return preco * imposto
impostos = [calcular_imposto(preco, 0.3) for preco in preco_produtos]


lista_aux = list(zip(preco_produtos,produtos))
lista_aux.sort(reverse=True)
produtos = [produto for vendas, produto in lista_aux]


meta = 1000
venda_produtos = [1500,150,2100,1950]

produtos_acima_da_meta = []

for i, produto in enumerate(produtos):
  if venda_produtos[i] > meta:
    produtos_acima_da_meta.append(produto)

#List Comprehensions
produtos_acima_da_meta = [produto for i, produto in enumerate(produtos)if venda_produtos[i] > meta]
