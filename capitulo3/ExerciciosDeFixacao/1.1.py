import math

a = float(input("Insira o valor de A: "))
b = float(input("Insira o valor de B: "))
c = float(input("Insira o valor de C: "))

delta = b**2 - 4 * a * c 

if delta > 0:
    print("A equação tem duas raízes reais e distintas")
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    raizes = "x1 = {:.2f}, x2 = {:.2f}".format(x1, x2)
elif delta == 0:
    print("A equação tem duas raízes reais e iguais")
    x = -b / (2 * a)
    raizes = "x = {:.2f}".format(x)
else:
    print("A equação não possui raízes reais, apenas raízes complexas")
    parte_real = -b / (2 * a)
    parte_imaginaria = math.sqrt(abs(delta)) / (2 * a)
    x1 = complex(parte_real, parte_imaginaria)
    x2 = complex(parte_real, -parte_imaginaria)
    raizes = "x1 = {}, x2 = {}".format(x1, x2)

print("Raízes calculadas:", raizes)
