senha = input("Digite sua senha com pelo menos cinco caracteres: ")
censura = "*" * len(senha[:-3])
digitosVisiveis = senha[-3:]
senhaF = censura+digitosVisiveis
print (f"A sua  senha é {senhaF}")