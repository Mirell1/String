email = input("Digite seu email: ")
while not email.endswith("@gmail.com"):
    email=input(f"email {email} incorreto! Digite novamente: ")
i = email.split('@')
usuario = i[0]
dominio = i[1]
print(f"O email {email} está correto, o usuario é {usuario} e o dominio é {dominio}")