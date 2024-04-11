H = float(input("Digite a altura do Cilindro: "))
R = float(input("Digite o raio do Cilindro: "))
Area = (3.14 * R * R) + (2 * 3.14 * R * H)
Litro = Area / 3
Qtde = Litro / 5
C = Qtde * 50
print("Esse é o custo total: R${} e essa é a quantidade de latas: {}".format(C, Qtde))