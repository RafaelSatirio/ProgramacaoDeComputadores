conjunto = [0] * (20)

con = 1
for i in range(0, 19 + 1, 1):
    print("Digite o " + str(con) + "° número do conjunto de 20")
    conjunto[i] = int(input())
    con = con + 1
con = 1
for i in range(0, 19 + 1, 1):
    if con == 1:
        menor = conjunto[i]
    else:
        if conjunto[i] < menor:
            menor = conjunto[i]
    con = con + 1
con = 1
for i in range(0, 19 + 1, 1):
    if con == 1:
        maior = conjunto[i]
    else:
        if conjunto[i] > maior:
            maior = conjunto[i]
    con = con + 1
print("O menor número do conjunto é: " + str(menor))
print("O maior número do conjunto é: " + str(maior))
