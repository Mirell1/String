placa = input("Digite a placa do seu veiculo para a verificação: ")  
i = len(placa)
letras = placa[:3]
numeros = placa[3:]
t_letra =  False
t_numero = False


if i == 7:
    for caractere in placa:
         if letras.isalpha():
            t_letra = True
         if numeros.isnumeric():
            t_numero = True
    if t_letra and t_numero:
        print(f"A placa {placa} é valida")
    else:
        print(f"A Placa {placa} não é valida")
else:
    print(f"A Placa {placa} não é valida")