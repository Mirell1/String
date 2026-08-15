nome_com = input("Digite seu nome completo: ")
norma = nome_com.lower()
separacao = norma.split(" ")
inicio = separacao[0]
letraInicial = inicio[:1]
fim = separacao[-1]
username = letraInicial+fim
print(f"O seu username baseado no seu nome completo é: {username}")