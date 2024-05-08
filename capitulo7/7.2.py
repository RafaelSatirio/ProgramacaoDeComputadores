def registrarDados():
    con = 0
    gastos = "Despesas.csv"
    outfile = open(Gastos, 'w')
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

# Main
vetCategorias = [""] * (5)
vetTotais = [0] * (6)

vetCategorias[0] = "Despesas Fixas"
vetCategorias[1] = "Transporte"
vetCategorias[2] = "Alimentação"
vetCategorias[3] = "Lazer"
vetCategorias[4] = "Saúde"
vetTotais[0] = 0
vetTotais[1] = 0
vetTotais[2] = 0
vetTotais[3] = 0
vetTotais[4] = 0
totalGeral = 0
registrarDados()
gastos = "Despesas.csv"
infile = open(Gastos, 'r')
nextLine = infile.readline()
