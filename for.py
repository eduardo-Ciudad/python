for i in range(10):
    print("chupa meu pau")

#estrutura for 

#for item in lista:
    #o que eu quero que seja executado varias vezes 

lista_precos = [1500, 1000, 800, 2000]

imposto = 0.1

for preco in lista_precos:
   imposto = preco * 0.1
   print(f"preco {preco}, imposto {imposto}")


#  regra de imposto
#  se o preco é ate 1000 -> 10% de imposto 
#  se o preco eh acima de 1000 -> 15% de imposto

for preco in lista_precos:
   if preco > 1000:
        imposto = preco * 0.15
   else:
        imposto = preco * 0.1
   print(f"preco {preco}, imposto {imposto}")

total_imposto = 0 #acumulado de um imposto
for preco in lista_precos: 
   if preco > 1000: 
        imposto = preco * 0.15  
   else:
        imposto = preco * 0.1
   print(f"preco {preco}, imposto {imposto}")
   total_imposto = total_imposto + imposto
print(total_imposto)

#exercicio 
vendas_22 = {"jan": 15000, "fev": 15500, "mar": 14000, "abr": 16600, "mai": 16300, "jun": 17000,}
vendas_23 = {"jan": 17000, "fev": 15500, "mar": 17500, "abr": 16900, "mai": 16000, "jun": 18500,}

#saber a variacao precentual cada mes 2023 em comparacao a 2022

#simulem: se a impresa tivesse pelo menos empatado  em 2022 nos messes que ela faturou menos q2ual seria o faturamento 

# primeira tentativa 


for mes in vendas_23:
    variacao = vendas_23[mes] - vendas_22[mes]
    if variacao < 0:
        variacao_negativa = variacao  * -1
        print(f"para que a variacao empate com a de 2022, a empresa precisaria vender {variacao_negativa} a mais do que vendeu ")
    else:
        print(f"mes {mes}, variacao {variacao}")

#correcao
faturamento_total_simulado = 0
for mes in vendas_23:
    valor_22 = vendas_22[mes]
    valor_23 = vendas_23[mes]
    var_percentual = valor_23 / valor_22 - 1
    if valor_23 < valor_22:
        faturamento_total_simulado = faturamento_total_simulado + valor_22
    else:
        faturamento_total_simulado = faturamento_total_simulado + valor_23
    print(f"mes {mes}, variacao percentual {var_percentual:.1%}")
    print(faturamento_total_simulado)


#jogo onde o computador escolhe um numero aleatorio e o jogador tenta adivinhar qual o numero escolhido pelo computador

import random  # 1

# 2 - O computador escolhe um número secreto entre 1 e 50
numero_secreto = random.randint(1, 50)

# 3 - Variável para contar quantas tentativas o jogador fez
tentativas = 0

print("=== Jogo do Número Secreto ===")
print("Tente adivinhar um número entre 1 e 50!")

# 4 - Laço de repetição: continua até o jogador acertar
while True:
    chute = int(input("Digite seu chute: "))  # 5
    tentativas += 1  # 6

    # 7 - Verificação com if
    if chute == numero_secreto:
        print(f"🎉 Parabéns! Você acertou em {tentativas} tentativas!")
        break  # 8 - Sai do loop quando acerta
    elif chute < numero_secreto:
        print("O número secreto é MAIOR.")
    else:
        print("O número secreto é MENOR.")


#fuçoes 

 #def funcao(parametro)

def se_inscrever():
     print("parabens vc se inscreveu")
se_inscrever()

for i in range(10):
    se_inscrever()  
 
