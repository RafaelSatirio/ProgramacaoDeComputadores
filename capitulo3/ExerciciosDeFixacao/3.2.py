import math

numero = float(input("Digite um número: "))

raiz = math.sqrt(numero)
raiz_int = int(raiz)
raiz_int_mais_um = raiz_int + 1

dif1 = raiz_int_mais_um - raiz
dif2 = raiz - raiz_int

if dif1 < dif2:
    inteiro_mais_proximo = raiz_int_mais_um
else:
    inteiro_mais_proximo = raiz_int


print(f"Raiz quadrada: {raiz}")
print(f"O número inteiro mais próximo da raiz quadrada de {numero} é: {inteiro_mais_proximo}")
