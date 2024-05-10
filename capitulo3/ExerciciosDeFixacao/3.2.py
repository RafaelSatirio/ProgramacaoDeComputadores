from math import sqrt

print("Digite um número para calcular sua raiz quadrada:")
num = int(input())
raizQ = sqrt(num)

print("A raiz quadrada desse número é:", raizQ)

num2 = int(raizQ)
num3 = raizQ + 1

print("num2:", num2)
print("num3:", num3)

diferenca = raizQ - num2
diferenca2 = num3 - raizQ

print("Diferença 1:", diferenca)
print("Diferença 2:", diferenca2)

if diferenca < diferenca2:
    numInteiro = int(raizQ)
    print("O número inteiro mais próximo da raiz quadrada de", num, "é:", numInteiro)
else:
    numInteiro = int(num3)
    print("O número inteiro mais próximo da raiz quadrada de", num, "é:", numInteiro)
