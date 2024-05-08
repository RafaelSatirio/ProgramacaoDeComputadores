def removerEspacosDireita(linha, tam):
    novaLinha = ""
    i = 1
    while i <= tam:
        i = i + 1

# Main
lin = 1
qtde = 0
infile = open("Drummond.txt", 'r')
nextLine = infile.readline()
while not nextLine == '':
    linha = nextLine
    nextLine = infile.readline()
    tam = len(linha)
    tamNovaLinha = 0
    novaLinha = ""
    for i in range(0, tam - 1 + 1, 1):
        car = linha[i]
        if car != "":
            tamNovaLinha = tamNovaLinha + 1
            novaLinha = car
    print("Linha" + str(lin) + " (" + str(tamNovaLinha) + " caracteres): " + linha)
    lin = lin + 1
    qtde = qtde + tamNovaLinha
print("Total de caracteres no arquivo: " + str(qtde))
