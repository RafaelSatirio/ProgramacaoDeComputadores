def saudacao(Nome, Hora):
    if Hora < 12 and Hora >= 4:
        Aux = "Bom Dia"
    elif Hora >= 12 and Hora < 19:
        Aux = "Boa Tarde"
    else:
        Aux = "Boa Noite"
    print("{}, {}!".format(Aux, Nome))


saudacao("Pedro", 10) 
saudacao("Pedro", 15) 
saudacao("Pedro", 3) 