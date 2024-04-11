print("Digite o preço do produto")
preco = float(input())
print("Digite a que região ele pertence " + "EX: 1 = Sul, " + "2 = Norte, " + "3 = Leste, " + "4 = Oeste, " + "7, 8, 9 = Sudeste, " + "10 até o 20 = Centro-Oeste, " + "5, 6, 25 até o 30, " + "nenhum desses = importado ")
origem = int(input())
if origem == 1:
    print("Preço: " + str(preco) + " Origem: Sul")
else:
    if origem == 2:
        print("Preço: " + str(preco) + " Origem: Norte")
    else:
        if origem == 3:
            print("Preço: " + str(preco) + " Origem: Leste")
        else:
            if origem == 4:
                print("Preço: " + str(preco) + " Origem: Oeste")
            else:
                if origem == 7 or origem == 8 or origem == 9:
                    print("Preço: " + str(preco) + " Origem: Sudeste")
                else:
                    if origem >= 10 or origem <= 20:
                        print("Preço: " + str(preco) + " Origem: Centro-Oeste")
                    else:
                        if origem == 5 or origem == 6 or origem >= 25 or origem <= 30:
                            print("Preço: " + str(preco) + " Origem: Nordeste")
                        else:
                            print("Preço: " + str(preco) + " Origem: Importado")
