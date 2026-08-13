telefone = input("Digite seu numero de telefone sem espaços ou caracteres ")
while not telefone.isdigit():
    print(f"O numero digitado: {telefone}, esta incorreto. Tente de novo")
    telefone = input("Digite seu numero novamente ")
    
i = len(telefone)
if i == 11:
    print(f"O numero digitado foi: {telefone}, esta correto")
elif i < 11:
    print(f"O numero digita foi: {telefone}, esta faltando caracteres")
else:
    print(f"O numero digitado foi: {telefone}, tem caracteres a mais")