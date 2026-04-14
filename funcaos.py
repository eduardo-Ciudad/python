lista_precos = [1500, 1000, 800, 2000]

total_imposto = 0 #acumulado 

def calcular_imposto(preco, aliquota1 = 0.2, aliquota2 = 0.15, aliquota3 = 0.1):
   if preco > 2000:
       imposto = preco * aliquota1
   elif preco > 1000:
       imposto = preco * aliquota2
   else:
       imposto = preco * aliquota3
   print(f"preco {preco}, imposto {imposto}")
   return imposto


for preco in lista_precos:
    imposto = calcular_imposto(preco, aliquota1 = 0.25)
    total_imposto = total_imposto + imposto

print(total_imposto)

def calcular_imposto2(preco, ir=0.345, csll= 0.05, iss=0.783):
    imposto_ir = preco * ir
    imposto_csll = preco * csll
    imposto_iss = preco * iss
    return imposto_ir, imposto_csll, imposto_iss

resposta = calcular_imposto2(1000)
print(resposta)