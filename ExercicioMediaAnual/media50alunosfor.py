acm = 0
for v in range(1, 50 + 1, 1):
    print("Digite a média anual do aluno = " + str(v))
    mA = float(input())
    acm = acm + mA
mAT = acm / 50
print("Média anual da turma = " + str(mAT))
