import pickle

class Abastecimento:
    def __init__(self, data, quilometragem, combustivel, litros, preco_litro):
        self.data = data
        self.quilometragem = quilometragem
        self.combustivel = combustivel
        self.litros = litros
        self.preco_litro = preco_litro

def ler_abastecimentos():
    try:
        with open("abastecimentos.pkl", "rb") as f:
            abastecimentos = pickle.load(f)
        return abastecimentos
    except FileNotFoundError:
        return []

def calcular_diferenca_preco(abastecimentos):
    diferenca_precos = [0]  # Inicializar a lista com 0 para o primeiro registro
    for i in range(1, len(abastecimentos)):
        diferenca = abastecimentos[i].preco_litro - abastecimentos[i - 1].preco_litro
        diferenca_precos.append(diferenca)
    return diferenca_precos

def calcular_consumo(abastecimentos):
    consumo = []
    for i in range(1, len(abastecimentos)):
        distancia = abastecimentos[i].quilometragem - abastecimentos[i - 1].quilometragem
        consumo_atual = distancia / abastecimentos[i].litros
        consumo_anterior = distancia / abastecimentos[i - 1].litros
        diferenca_consumo = consumo_atual - consumo_anterior
        consumo.append((consumo_atual, diferenca_consumo))
    return consumo

# Ler os abastecimentos
abastecimentos = ler_abastecimentos()

# Calcular a diferença de preço em relação ao abastecimento anterior
diferenca_precos = calcular_diferenca_preco(abastecimentos)

# Calcular o consumo e a diferença para o consumo anterior
consumo = calcular_consumo(abastecimentos)

# Mostrar o relatório
print("Relatório de Abastecimentos:")
print("{:<12} {:<15} {:<15} {:<10} {:<10} {:<20} {:<20}".format("Data", "Quilometragem", "Combustível", "Litros", "Preço/Litro", "Dif. Preço Anterior", "Consumo (km/l)"))
for i in range(len(abastecimentos) - 1):  # Removido o -1 para incluir todos os registros
    print("{:<12} {:<15} {:<15} {:<10.2f} {:<10.2f} {:<20.2f} {:<20.2f}".format(
        abastecimentos[i + 1].data,  # Adicionado +1 para evitar o primeiro registro
        abastecimentos[i + 1].quilometragem,  # Adicionado +1 para evitar o primeiro registro
        abastecimentos[i + 1].combustivel,  # Adicionado +1 para evitar o primeiro registro
        abastecimentos[i + 1].litros,  # Adicionado +1 para evitar o primeiro registro
        abastecimentos[i + 1].preco_litro,  # Adicionado +1 para evitar o primeiro registro
        diferenca_precos[i],
        consumo[i][0]
    ))
