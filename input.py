nome = input("digite aqui seu nome: ")
print(nome)
email = input("digite aqui seu email: ")


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



