def calcular_imposto2(preco, ir=0.345, csll= 0.05, iss=0.783):
    imposto_ir = preco * ir
    imposto_csll = preco * csll
    imposto_iss = preco * iss
    return imposto_ir, imposto_csll, imposto_iss

resposta = calcular_imposto2(1000)
ir, csll, iss = resposta
print(ir, csll, iss, sep="\n")

tamanho_tela = (1920, 1080)
print(tamanho_tela)

#(345.0, 50.0, 783.0) -> imutavel

#exercicio 
vendas = {
"Andre":  [1000, 500, 300, 5000, 1500, 80, 3000],
"Andressa": [1500, 9000, 300, 150, 1500, 120, 130, 55, 500, 8500],
"Alan": [800, 100],
"Ana": [800, 900, 950, 1200, 130, 50, 50, 50, 50, 65, 60, 70, 70, 70, 200, 180,]
}

#calcular o bonus de cada vendedor , cada venda o vendedor ganha 2 reais e 1% do valor de cada venda , calcular o valor total de vendas pago a cada vendedor


 



    #ou 
def calcular_bonus(lista_vendas):
    qtde = len(lista_vendas)
    bonus1 = qtde * 2
    valor_total = sum(lista_vendas)
    bonus2 = 0.01 * valor_total
    bonus = bonus1 + bonus2
    return bonus

bonus_total = 0
for vendedor in vendas:
    lista_vendas_vendedor = vendas[vendedor]
    bonus = calcular_bonus(lista_vendas_vendedor)
    print(f"vendedor: {vendedor}, bonus: {bonus}")
    bonus_total = bonus_total + bonus

for vendedor in vendas:
    

