arquivo = "output.json"
infile = open(arquivo, 'r')
nextLine = infile.readline()
while not nextLine == '':
    contatosJSON = nextLine
    nextLine = infile.readline()
    tam = len(contatosJSON)
    con = 1
    linhaSemChaves = ""
    for i in range(0, tam - 1 + 1, 1):
        caractere = contatosJSON[i]
        if caractere != "{" and caractere != "}":
            if caractere != "1" and caractere != "2" and caractere != "3":
                if caractere != ":":
                    if caractere != ",":
                        if caractere != "":
                            linhaSemChaves = linhaSemChaves + caractere
    print(linhaSemChaves)
