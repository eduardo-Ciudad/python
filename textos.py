
faturamento = 1000
custo = 700

lucro = faturamento - custo

print(f"faturamento: {faturamento}, custo: {custo}, lucro: {lucro}")
print("faturamento:" + str(faturamento) + ", custo:" + str(custo) + ", lucro:" + str(lucro))

email = "email_falso@gmail.com"
        #01234567891011... o python coloca o indice dew cada caractere
        #o @ é o caractere de indice 11 
        #o .find mostra o indice do caractere

print(email.lower()) #.lower coloca o email em minusculo
print(email.find("@"))
print(email.find("."))#-1 se ele não econtrar o caractere
print(email[11]) #mostra o caractere de indice 11

posicao = email.find("@")
servidor = email[posicao+1:]

print(servidor)

nome_email = email[:posicao]
print(nome_email)

#tamanho de um texto

tamanho = len(email)
print(tamanho)

#trocar um pedaço de um texto 

email_trocado = email.replace("gmail.com", "hotmail.com")
print(email_trocado)

nome = "eduardo ciudad"
print(nome.capitalize())#coloca apenas a primeira letra em maiusculo
print(nome.title()) #coloca a primeira letra de cada palavra em maiusculo

#especiais
margem = lucro / faturamento
print(f"faturamento: R${faturamento:,.2f}\n custo: {custo}\n lucro: {lucro}")
#.2f = "." = tem casa decimal, "2" = 2 casas decimais,"f" = float
print(f"margem: {margem:.1%}")

#exercicio
nome = "Eduardo Ciudad Figueredo"
email = "eduardo_falso2@gmail.com"

#descubra o servidor do email

posicao = email.find("@")
servidor = email[posicao:]
print(servidor)

#pegar o primeiro nome do usuario

posicao = nome.find(" ")
primeiro_nome = nome[ : posicao]
print(primeiro_nome)

#construa uma mensage: USuario primeiro nome  cadastrado com sucesso com o email email_falso2@gmai

mensagem = f"usuario {primeiro_nome} cadastrado com sucesso com o email: {email}"
print(mensagem)

# construa uma mesnsagem : enviamos um link de confirmação para o email E*****@gmail.com
primeira_letra = email[0]
mensagem_2 = f"enviamos um link de confirmacao {primeira_letra}***{servidor}"
print(mensagem_2)



