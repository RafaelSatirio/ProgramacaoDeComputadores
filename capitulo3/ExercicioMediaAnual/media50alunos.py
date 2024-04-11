aluno = 1
con = 0
while con < 50:
    print("Aluno: " + str(aluno))
    print("Digite o valor da nota 1")
    n1 = float(input())
    print("Digite o valor da nota 2")
    n2 = float(input())
    print("Digite o valor da nota 3")
    n3 = float(input())
    print("Digite o valor da nota 4")
    n4 = float(input())
    mA = (n1 + n2 + n3 + n4) / 4
    print("Média Anual: " + str(mA))
    if mA >= 7:
        print("Aluno Aprovado")
        print("Parabéns pra ele!")
    else:
        print("Aluno Reprovado")
        print("Ele tem que estudar mais!")
    con = con + 1
    aluno = aluno + 1
