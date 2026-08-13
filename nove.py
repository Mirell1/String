cnpj = input("Digite seu CNPJ: ")
cnpjN = cnpj.replace(".","").replace("/","").replace("-","")
verificacao = len(cnpjN)
if verificacao == 14:
    print(f"O CNPJ {cnpjN} é valido")
#else: 
    #print(f"O CNPJ {cnpjN} é invalido") - a professora pediu so ate aqui, mas eu quis deixar mais longo
elif verificacao < 14: 
    print(f"O CNPJ {cnpjN} é invalido pois tem menos que 14 caracteres")
elif verificacao > 14: 
    print(f"O CNPJ {cnpjN} é invalido pois tem mais que 14 caracteres")