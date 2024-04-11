con = 0
acm = 0
n = 1
while n > 0 and con < 2:
    print("Digite um número par")
    n = int(input())
    if n > 0 and n % 2 == 0:
        acm = acm + n
        con = con + 1
    else:
        print("nenhum par foi fornecido!")
if con > 0:
    mnp = float(acm) / con
    print("Média dos números pares: " + str(mnp))
