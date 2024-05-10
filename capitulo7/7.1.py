con = 0
gastos = "Despesas.csv"
outfile = open(gastos, 'w')
print("Digite o dia da despesa")
dia = int(input())
while dia != 0:
    if con == 0:
        con = con + 1
        print("Digite o mes")
        mes = int(input())
        print("Digite a categoria")
        categoria = int(input())
        print("Digite o valor")
        valor = float(input())
        print("Digite a descrição")
        descricao = input()
        outfile.write(str("Dia" + ";" + "Mes" + ";" + "Categoria" + ";" + "Valor" + ";" + "Descricao") + '\n')
        outfile.write(str(str(dia) + ";" + str(mes) + ";" + str(categoria) + ";" + str(valor) + ";" + descricao) + '\n')
        print("Digite o dia da despesa(0 para terminar)")
        dia = int(input())
    else:
        print("Digite o mes")
        mes = int(input())
        print("Digite a categoria")
        categoria = int(input())
        print("Digite o valor")
        valor = float(input())
        print("Digite a descrição")
        descricao = input()
        outfile.write(str(str(dia) + ";" + str(mes) + ";" + str(categoria) + ";" + str(valor) + ";" + descricao) + '\n')
        print("Digite o dia da despesa(0 para terminar)")
        dia = int(input())
