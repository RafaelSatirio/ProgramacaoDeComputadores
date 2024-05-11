print("Digite um número para descobrir o h")
n = int(input())
h = 0
for i in range(1, n + 1, 1):
    h = h + float(1) / i
print("O H é: " + str(h))
