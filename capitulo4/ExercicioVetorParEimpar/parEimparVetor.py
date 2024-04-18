vetLido = [0] * (11)
vetPar = [0] * (11)
vetImpar = [0] * (11)

for x in range(1, 10 + 1, 1):
    print("Número: " + str(x))
    vetLido[x] = int(input())
i = 0
p = 0
for x in range(1, 10 + 1, 1):
    if vetLido[x] % 2 == 0:
        p = p + 1
        vetPar[p] = vetLido[x]
    else:
        i = i + 1
        vetImpar[i] = vetLido[x]
for x in range(1, 10 + 1, 1):
    print("VetLido: " + str(vetLido[x]))
for x in range(1, 10 + 1, 1):
    print("VetPar: " + str(vetPar[x]))
for x in range(1, 10 + 1, 1):
    print("VetImpar: " + str(vetImpar[x]))
