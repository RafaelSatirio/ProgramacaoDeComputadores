conv = 0
ct = 0
cb = 0
cr = 0
finalizador = ""


while True:
    print("Escolha o tipo de vinho")
    print("B = branco")
    print("T = Tinto")
    print("R = Rosé")

    tv = str(input("")).upper()

    if tv == "B":
        cb += 1
        print("Adicionado um vinho Branco ao estoque")
    elif tv == "T":
        ct += 1
        print("Adicionado um vinho Tinto ao estoque")
    elif tv == "R":
        cr += 1
        print("Adicionado um vinho Rosé ao estoque")
    else:
        print("Tipo de vinho inválido!")


    conv = conv + 1

    print("Deseja finalizar a contagem?")
    finalizador = str(input("Se sim digite = finalizar "))

    if finalizador.lower() == "finalizar" :
        break

if conv > 0:
    pt = (ct*100) / conv
    pb = (cb*100) / conv
    pr = (cr*100) / conv
    print("Porcentagem de Tintos = {}".format(pt))
    print("Porcentagem de Brancos = {}".format(pb))
    print("Porcentagem de Rosés = {}".format(pr))
else:
    print("Nenhum tipo de vinho foi fornecido!")