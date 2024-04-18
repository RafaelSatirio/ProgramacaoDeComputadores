vetLido = [0] * (11)
vetDes = [0] * (11)

soma = 0

for x in range(1, 10 + 1, 1):
    print("Digite o {} número para fazer a média".format(x))
    vetLido[x] = float(input())
    soma = soma + vetLido[x]

mediaLido = soma / 10

soma = 0 

for x in range(1, 10 + 1, 1):
    vetDes[x] = abs(vetLido[x] - mediaLido)
    soma = soma + vetDes[x]

mediaDes = soma / 10

print("A média do vetLido: {} e a média do vetDes: {}".format(mediaLido, mediaDes))