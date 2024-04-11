con = 0
acm = 0
mA = 0
aluno = 1
while mA != -1:
    print("Digite a média do aluno: " + str(aluno))
    mA = float(input())
    if mA != -1:
        acm = acm + mA
        con = con + 1
        aluno = aluno + 1
if con > 0:
    mAT = acm / con
    print("Média anual da turma: " + str(mAT))
else:
    print("Nenhuma média válida fornecida")
