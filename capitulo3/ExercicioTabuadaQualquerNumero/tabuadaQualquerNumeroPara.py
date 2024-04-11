print("Digite um número para gerar a tabuada")
n = int(input())
for x in range(1, 10 + 1, 1):
    con = 1
    for con in range(1, 10 + 1, 1):
        print(str(con) + " X " + str(n) + " = " + str(con * 5))
