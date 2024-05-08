import pickle

class Abastecimento:
    def __init__(self, data, quilometragem, combustivel, litros, preco_litro):
        self.data = data
        self.quilometragem = quilometragem
        self.combustivel = combustivel
        self.litros = litros
        self.preco_litro = preco_litro

def registrar_abastecimento():
    abastecimentos = []

    while True:
        data = input("Data do abastecimento (DD/MM/AAAA) ou '0' para encerrar: ")
        if data == '0':
            break
        quilometragem = float(input("Quilometragem do veículo: "))
        combustivel = input("Tipo de combustível: ")
        litros = float(input("Quantidade de litros abastecidos: "))
        preco_litro = float(input("Preço do litro: "))

        abastecimento = Abastecimento(data, quilometragem, combustivel, litros, preco_litro)
        abastecimentos.append(abastecimento)

    with open("abastecimentos.pkl", "wb") as f:
        pickle.dump(abastecimentos, f)

def ler_abastecimentos():
    try:
        with open("abastecimentos.pkl", "rb") as f:
            abastecimentos = pickle.load(f)
        return abastecimentos
    except FileNotFoundError:
        return []

def exibir_abastecimentos(abastecimentos):
    print("Abastecimentos:")
    print("{:<12} {:<15} {:<15} {:<10} {:<10}".format("Data", "Quilometragem", "Combustível", "Litros", "Preço/Litro"))
    for abastecimento in abastecimentos:
        print("{:<12} {:<15} {:<15} {:<10.2f} {:<10.2f}".format(abastecimento.data, abastecimento.quilometragem, abastecimento.combustivel, abastecimento.litros, abastecimento.preco_litro))

# Registrar os abastecimentos
registrar_abastecimento()

# Ler e exibir os abastecimentos
abastecimentos = ler_abastecimentos()
exibir_abastecimentos(abastecimentos)
