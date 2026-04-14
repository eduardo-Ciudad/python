
vendas = [100, 50, 130, 80, 120]

print(vendas[-1])

total_vendas = sum(vendas)
print(total_vendas)
quantidade = len(vendas)
print(quantidade)
valor_max = max(vendas)
valor_min = min(vendas)
print(valor_max, valor_min)

posicao = vendas.index(130)
print(posicao)
print(vendas[2:])

produtos = ["iphone", "ipad", "airpod"]
precos = [4000, 8000, 2000]


print("airpod" in produtos)
precos[0] = 5000 #editar o valor dentro de uma lista
print(precos)

precos[0] = precos[0] * 1.1
print(precos)

#adiciona um produto
produtos.append("macbook")
precos.append(1000)
print(produtos)
print(precos)

#remover um produto
produtos.remove("ipad")
precos.pop(-1)
print(produtos)
print(precos)

#inserir um valor
produtos.insert(1, "tablet")

#contar valores
print(produtos.count("ipad"))

#ordernar
precos.sort(reverse=True)
print(precos)