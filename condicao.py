faturamento = 1000
custo = 8800

lucro = faturamento - custo

#if condicao (comparacao):
    # tudo o que vc quer q aconteca se a condicao for verdadeira

if lucro >= 0:
    print("lucro:",lucro)
else:
    #tudo o que vc quer q aconteca se a condicao for falsa
    print("prejuizo!!")
    print(lucro)

#produtos = ["iphone", "ipad", "airpod"]
#novo_produto = input("digite o novo produto: ")
#novo_produto = novo_produto.lower()

#if novo_produto in produtos:
   #print("produto já cadastrado")
#else:
   #print("produto cadastrado com sucesso")
   # produtos.append(novo_produto)
    
#pint(produtos)

#acima de 15000 -> 500 bonus
#acima de 10000 -> 150 bonus
#acima de 5000 -> 50 bonus

vendas = 15000

if vendas >= 15000:
    bonus = 500
#caso contario se 
elif vendas > 10000:
    bonus = 150

elif vendas > 5000:
    bonus = 50

else:
    bonus = 0

#print("bonus:", bonus)





#acima de 15000 -> 500 bonus
#acima de 10000 -> 150 bonus
#acima de 5000 -> 50 bonus
#vendas da empresa > 500000


vendas = 17000
vendas_empresa = 600000
meta_empresa = 500000


if vendas >= 15000 and vendas_empresa >= meta_empresa:
    bonus = 500

elif vendas >= 10000 and vendas_empresa >= meta_empresa:
    bonus = 150

elif vendas >= 5000 and vendas_empresa >= meta_empresa:
    bonus = 50

else:
    bonus = 0

print("bonus:", bonus)