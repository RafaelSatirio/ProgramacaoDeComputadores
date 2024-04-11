notaAcima = 0
print("Digite a nota do Aluno A")
a = int(input())
print("Digite a nota do Aluno B")
b = int(input())
print("Digite a nota do Aluno C")
c = int(input())
print("Digite a nota do Aluno D")
d = int(input())
print("Digite a nota do Aluno E")
e = int(input())
print("Digite a nota do Aluno F")
f = int(input())
print("Digite a nota do Aluno G")
g = int(input())
print("Digite a nota do Aluno H")
h = int(input())
print("Digite a nota do Aluno I")
i = int(input())
print("Digite a nota do Aluno J")
j = int(input())
mediaTurma = float(a + b + c + d + e + f + g + h + i + j) / 10
print("Média da turma = " + str(mediaTurma))
if a > mediaTurma:
    notaAcima = notaAcima + 1
if b > mediaTurma:
    notaAcima = notaAcima + 1
if c > mediaTurma:
    notaAcima = notaAcima + 1
if d > mediaTurma:
    notaAcima = notaAcima + 1
if e > mediaTurma:
    notaAcima = notaAcima + 1
if f > mediaTurma:
    notaAcima = notaAcima + 1
if g > mediaTurma:
    notaAcima = notaAcima + 1
if h > mediaTurma:
    notaAcima = notaAcima + 1
if i > mediaTurma:
    notaAcima = notaAcima + 1
if j > mediaTurma:
    notaAcima = notaAcima + 1
print("Quantidades de alunos com nota acima da média =  " + str(notaAcima))
