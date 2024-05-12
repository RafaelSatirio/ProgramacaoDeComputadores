print("Digite um número para calcular o seu fatorial")
n = int(input())
if n == 0:
    print("O fatorial de: " + str(n) + " é: 1")
else:
    fatorial = 1
    for i in range(1, n + 1, 1):
        fatorial = fatorial * i
    print("O fatorial do número: " + str(n) + " é: " + str(fatorial))
