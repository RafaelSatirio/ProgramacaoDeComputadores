mediaPonderada = [0] * (5)
pesos = [0] * (5)
numero = [0] * (5)

con = 1
for i in range(0, 4 + 1, 1):
    print("Digite o " + str(con) + "° de 5")
    numero[i] = int(input())
    con = con + 1
con = 1
pesos[0] = 0
for i in range(0, 4 + 1, 1):
    pesos[i] = con
    con = con + 1
con = 1
for i in range(0, 4 + 1, 1):
    mediaPonderada[i] = numero[i] * pesos[i]
mediaPonderadaResultado = 0
mediaPonderadaResultado = mediaPonderada[0] + mediaPonderada[1] + mediaPonderada[2] + mediaPonderada[3] + mediaPonderada[4]
mediaPonderadaResultado = float(mediaPonderadaResultado) / (pesos[0] + pesos[1] + pesos[2] + pesos[3] + pesos[4])
print("A média ponderada é: " + str(mediaPonderadaResultado))
