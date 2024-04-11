N1 = float(input("Digite sua nota 1: "))
N2 = float(input("Digite sua nota 2: "))
N3 = float(input("Digite sua nota 3: "))
N4 = float(input("Digite sua nota 4: "))

MA = (N1 + N2 + N3 + N4) / 4

print("Sua média é: {}".format(MA))

if MA >= 7:
    print("Você foi aprovado!")
else:
    print("Você foi reprovado!")