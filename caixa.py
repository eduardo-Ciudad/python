valor_saque = int(input("digite o valor do saque: "))

nota_100 = valor_saque // 100
resto = valor_saque % 100

nota_50 = resto // 50
resto = resto % 50

nota_10 = resto // 10
resto = resto % 10

nota_5 = resto // 5
resto = resto % 5

nota_2 = resto // 2
resto = resto % 2

print(f"notas de 100: {nota_100}")
print(f"notas de 50: {nota_50}")
print(f"notas de 10: {nota_10}")
print(f"notas de 5: {nota_5}")
print(f"notas de 1: {nota_2}")