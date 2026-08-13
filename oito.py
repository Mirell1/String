palavra = input("Digite uma palavra: ")
palavraN = palavra.lower()
revertida = palavraN[::-1]
if palavraN == revertida:
    print("Essa palavra é um palíndromo")
else: 
    print("Essa palavra não é um palíndromo")
