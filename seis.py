arquivo = input("Diga o nome do arquivo da qual deseja fazer o upload junto de sua extensão ")
if arquivo.endswith("jpg"):
    print("Arquivo é aceito")
elif arquivo.endswith("png"):
    print("Arquivo é aceito")
else:
    print('Arquivo nao aceito, faça upload apenas de arquivos na extensao "png" ou "jpg"')
