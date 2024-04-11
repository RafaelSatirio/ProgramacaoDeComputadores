con = 0
soma = 0
mediaTurma = 0
while con < 10:
    print("Digite a media do aluno: " + str(con + 1))
    mediaAnual = float(input())
    soma = soma + mediaAnual
    con = con + 1
mediaTurma = soma / 10
print("Média anual da turma = " + str(mediaTurma))
