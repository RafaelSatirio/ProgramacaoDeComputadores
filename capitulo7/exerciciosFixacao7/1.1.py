import pickle

class Medicao:
    def __init__(self, data, altura, peso, cintura, abdomen, quadril):
        self.data = data
        self.altura = altura
        self.peso = peso
        self.cintura = cintura
        self.abdomen = abdomen
        self.quadril = quadril

def registrar_medicao():
    medidas = []

    while True:
        data = input("Data da medição (DD/MM) ou '0' para encerrar: ")
        if data == '0':
            break
        altura = float(input("Altura (m): "))
        peso = float(input("Peso (kg): "))
        cintura = float(input("Cintura (cm): "))
        abdomen = float(input("Abdômen (cm): "))
        quadril = float(input("Quadril (cm): "))

        medicao = Medicao(data, altura, peso, cintura, abdomen, quadril)
        medidas.append(medicao)

    with open("medicoes.pkl", "wb") as f:
        pickle.dump(medidas, f)

def ler_medicoes():
    try:
        with open("medicoes.pkl", "rb") as f:
            medidas = pickle.load(f)
        return medidas
    except FileNotFoundError:
        return []

def exibir_medicoes(medidas):
    print("Medições:")
    print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("Data", "Altura (m)", "Peso (kg)", "Cintura (cm)", "Abdômen (cm)", "Quadril (cm)"))
    for medicao in medidas:
        print("{:<10} {:<10.2f} {:<10.2f} {:<10.2f} {:<10.2f} {:<10.2f}".format(
            medicao.data,
            medicao.altura,
            medicao.peso,
            medicao.cintura,
            medicao.abdomen,
            medicao.quadril
        ))

# Registrar as medições
registrar_medicao()

# Ler e exibir as medições
medidas = ler_medicoes()
exibir_medicoes(medidas)
