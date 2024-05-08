listaCompras = "mercado.txt"
print("Qual item deseja incluir?(escreva 'fim' se quiser terminar)")
item = input()
outfile = open(listaCompras, 'w')
outfile.write(str(item) + '\n')
while item != "fim":
    print("Qual item deseja incluir?(escreva 'fim' se quiser terminar)")
    item = input()
    if item == "fim":
        pass
    else:
        outfile.write(str(item) + '\n')
