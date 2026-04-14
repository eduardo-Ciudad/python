#Tabuada

#O usuário digita um número e o programa mostra a tabuada desse número de 1 a 10.

#Exemplo: número 7 → imprime 7x1, 7x2 … até 7x10.

numero = int(input("Digite um número para ver sua tabuada: "))

for i in range (1,11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
   
