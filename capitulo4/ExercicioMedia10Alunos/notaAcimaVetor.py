vetClasse = [0] * (11)

soma = 0
notaAcima = 0
for x in range(1, 10 + 1, 1):
    print("digite a nota do aluno: " + str(x))
    vetClasse[x] = float(input())
for x in range(1, 10 + 1, 1):
    soma = soma + vetClasse[x]
media = soma / 10
for x in range(1, 10 + 1, 1):
    if vetClasse[x] > media:
        notaAcima = notaAcima + 1
print("Números de alunos com a nota acima da média = " + str(notaAcima))
