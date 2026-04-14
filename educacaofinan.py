taxa = float(input("digite a taxa: "))
deposito = float(input("digite o deposito: "))
numero_depositos = int(input("digite o numero de depositos: "))
 
montante = deposito * ((1 + taxa) **  numero_depositos - 1) / ((1 + taxa) ** taxa - 1)

print(f"Ao final de {numero_depositos} meses, você terá: R${montante:.2f}")
