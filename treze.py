palavra = input("Digite uma a palavra: ")
minuscula = palavra.lower()
s_espaco = minuscula.strip()
norma = s_espaco.replace(" ","")
vogais = ["a","e","i","o","u"]

if not norma.isalpha():
    print("Por favor, digite apenas letras.")
elif any(letra in norma for letra in vogais):
    print(f"A palavra {norma} tem vogais")
else:
    print(f"A palavra {norma} só tem consoantes")