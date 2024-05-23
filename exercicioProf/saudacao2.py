def saudacao(Nome, Hora, Titulo=""):
    if Hora < 12 and Hora >= 4:
        Aux = "Bom Dia"
    elif Hora >= 12 and Hora < 19:
        Aux = "Boa Tarde"
    else:
        Aux = "Boa Noite"
    print("{}, {} {}!".format(Aux, Titulo, Nome))

saudacao("Pedro", 10) 
saudacao("Pedro", 15) 
saudacao("Pedro", 3) 

saudacao(Hora = 15, Nome = "Pedro")
saudacao(Nome = "Pedro", Hora = 15,  Titulo = "Dr.")
saudacao(Nome = "Pedro", Hora = 15, Titulo = "São")