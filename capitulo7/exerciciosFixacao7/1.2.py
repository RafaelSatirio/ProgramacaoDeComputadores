import pickle

class Medicao:
    def __init__(self, data, altura, peso, cintura, abdomen, quadril):
        self.data = data
        self.altura = altura
        self.peso = peso
        self.cintura = cintura
        self.abdomen = abdomen
        self.quadril = quadril

def ler_medicoes():
    try:
        with open("medicoes.pkl", "rb") as f:
            medidas = pickle.load(f)
        return medidas
    except FileNotFoundError:
        return []

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def calcular_imc_razao(medidas):
    imcs = []
    razoes_cintura_quadril = []
    diferenca_peso = []

    for i in range(1, len(medidas)):
        imc = calcular_imc(medidas[i].peso, medidas[i].altura)
        imcs.append(imc)
        
        razao_cintura_quadril = medidas[i].cintura / medidas[i].quadril
        razoes_cintura_quadril.append(razao_cintura_quadril)
        
        dif_peso = medidas[i].peso - medidas[i - 1].peso
        diferenca_peso.append(dif_peso)

    return imcs, razoes_cintura_quadril, diferenca_peso

def calcular_imc_razao_media(imcs, razoes_cintura_quadril, diferenca_peso):
    imc_media = sum(imcs) / len(imcs)
    razao_cintura_quadril_media = sum(razoes_cintura_quadril) / len(razoes_cintura_quadril)
    dif_peso_media = sum(diferenca_peso) / len(diferenca_peso)
    
    return imc_media, razao_cintura_quadril_media, dif_peso_media

# Ler as medições
medidas = ler_medicoes()

# Calcular IMC, razão cintura-quadril, diferença de peso, IMC médio, razão cintura-quadril média e diferença de peso média
imcs, razoes_cintura_quadril, diferenca_peso = calcular_imc_razao(medidas)
imc_media, razao_cintura_quadril_media, dif_peso_media = calcular_imc_razao_media(imcs, razoes_cintura_quadril, diferenca_peso)

# Obter as datas das medições
datas = [medida.data for medida in medidas]

# Mostrar o relatório
print("Relatório de Medições:")
print("{:<12}".format("Data"), end="")
for data in datas:
    print("{:<15}".format(data), end="")
print("\n{:15} {:<10} {:<10} {:<10} {:<10}".format("", "Altura (m)", "Peso (kg)", "Cintura (cm)", "Abdômen (cm)"))
for i in range(1, len(medidas)):
    print("{:<12}".format(medidas[i].data), end="")
    print("{:<15.2f} {:<10.2f} {:<10.2f} {:<10.2f}".format(
        medidas[i].altura,
        medidas[i].peso,
        medidas[i].cintura,
        medidas[i].abdomen
    ))
    print("{:<12}".format("Cintura"), end="")
    print("{:<10} {:<10} {:<10}".format(
        "",
        "",
        medidas[i].quadril
    ))

# Mostrar médias
print("\nMédia:")
print("IMC Médio: {:.2f}".format(imc_media))
print("Razão Cintura/Quadril Média: {:.2f}".format(razao_cintura_quadril_media))
print("Diferença de Peso Média: {:.2f}".format(dif_peso_media))
