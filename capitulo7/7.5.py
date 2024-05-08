print("Qual nome deseja por no arquivo?(escreva '.txt' depois do nome)")
listaCompras = input()
con = 1
print("Qual o " + str(con) + "° item deseja incluir?(escreva 'fim' se quiser terminar)")
item = input()
outfile = open(listaCompras, 'w')
while item != "fim":
    print("Qual a quantidade do item?")
    qtde = int(input())
    linha = "item " + str(con) + ": " + str(qtde) + " - " + str(item)
    outfile.write(str(linha) + '\n')
    con = con + 1
    print("Qual o " + str(con) + "° item deseja incluir?(escreva 'fim' se quiser terminar)")
    item = input()
