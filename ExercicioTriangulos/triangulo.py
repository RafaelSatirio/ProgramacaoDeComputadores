print("Programa pra descobrir o tipo de triângulo")
print("Digite o valor de A")
a = int(input())
print("Digite o valor de B")
b = int(input())
print("Digite o valor de C")
c = int(input())
if a < b + c and b < a + c and c < a + b:
    if a == b and b == c:
        print("Triângulo Equilátero")
    else:
        if a == b or b == c or a == c:
            print("Triângulo Isósceles")
        else:
            print("Triãngulo Escaleno")
else:
    print("Os valores que você digitou não formam um triângulo")
