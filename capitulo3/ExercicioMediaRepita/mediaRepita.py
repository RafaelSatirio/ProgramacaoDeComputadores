con = 0
acm = 0
aluno = 1

while True:
    print("Digite a Média do Aluno {}".format(aluno))
    MA = float(input())
    acm = acm + MA
    con = con + 1
    aluno = aluno +1
    if con >= 50:
        break
MAT = acm / 50
print("Média anual da Turma: {}".format(MAT))

