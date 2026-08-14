senha = input("Digite sua senha com pelo menos cinco caracteres: ")
censura = "*" * len(senha[2:-2])
digitosVisiveis = senha[-2:]
inicio = senha[0:2]
senhaF = inicio+censura+digitosVisiveis
print (f"A sua  senha é {senhaF}")