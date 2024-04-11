con = 0
acm = 0
aluno = 1
while con < 50:
    print("Digite a média do aluno: " + str(aluno))
    mA = float(input())
    acm = acm + mA
    con = con + 1
    aluno = aluno + 1
MAT = acm / 50
print("Média anual da turma é: " + str(MAT))
