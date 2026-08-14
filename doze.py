senha = input("Dgite sua senha: ")
tem_letra = False
tem_numero = False
i = len(senha)
if i >= 8:
    for caractere in senha:
        if caractere.isalpha():
            tem_letra = True
        if caractere.isdigit():
            tem_numero = True
    if tem_letra and tem_numero:
                print("A senha é forte!")
    else:
                print("A senha é fraca.")
else:
    print("A senha é fraca.")