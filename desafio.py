# exercicio desafio
# sectema de consulta de precos

precos = [1500, 1000, 800, 2000]
produtos = ["celular", "camera", "fone de ouvido", "monitor"]

produto_novo = input("digite o produto que deseja consultar o preco: ")
produto_novo = produto_novo.lower()

if produto_novo in produtos:
    posicao = produtos.index(produto_novo)
    preco = precos[posicao]
    print(f"o preco do {produto_novo} eh: {preco}")
else:
    print("produto nao cadastrada")