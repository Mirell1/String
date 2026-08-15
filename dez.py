email = input("Digite seu email corporativo: ")
while not email.endswith("@hashtag.com"):
    email=input(f"email {email} incorreto! Digite novamente: ")
print(f"O email {email} está correto, validando acesso...")