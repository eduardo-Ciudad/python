precos = [1500, 1000, 800, 2000]
produtos = ["celular", "camera", "fone de ouvido", "monitor"]

dic_precos = {
    "celular": 1500,
    "camera": 1000,
    "fone de ouvido": 800,
    "monitor": 2000
}

#pegar um item do dicionario 

preco_celular = dic_precos["celular"]
print(preco_celular)

dic_precos['celular'] = 2000
print(dic_precos)

dic_precos['iphone'] = 4000
print(dic_precos)

dic_precos.pop("celular")
print(dic_precos)

#tamanho do dicionario]

print(len(dic_precos))

#verificar se um item existe ou nao

print("celular" in dic_precos) #item 
print(dic_precos.keys())
print(dic_precos.values())

#exercicio

dic_precos = {
    "celular": 1500,
    "camera": 1000,
    "fone de ouvido": 800,
    "monitor": 2000
}

produto_procurado = input("digite o produto que deseja consultar o preco: ")
produto_procurado = produto_procurado.lower()

if produto_procurado in dic_precos:
    preco = dic_precos[produto_procurado]
    print(f"o preco do {produto_procurado} eh: {preco}")
else:
    print("produto nao cadastrado")