import pickle

class Despesa:
    def __init__(self, dia, mes, categoria, valor, descricao):
        self.dia = dia
        self.mes = mes
        self.categoria = categoria
        self.valor = valor
        self.descricao = descricao

# Função para criar o arquivo de despesas
def criar_despesas():
    despesas = []

    print("Digite o dia da despesa (0 para terminar)")
    dia = int(input())

    while dia != 0:
        mes = int(input("Digite o mês: "))
        print("Categorias:")
        print("1: Despesas fixas")
        print("2: Transporte")
        print("3: Alimentação")
        print("4: Lazer")
        print("5: Saúde")
        categoria = int(input("Digite a categoria (1 a 5): "))
        valor = float(input("Digite o valor: "))
        descricao = input("Digite a descrição: ")

        despesa = Despesa(dia, mes, categoria, valor, descricao)
        despesas.append(despesa)

        print("Digite o dia da despesa (0 para terminar)")
        dia = int(input())

    with open("despesas.pkl", "wb") as f:
        pickle.dump(despesas, f)

# Função para ler o arquivo de despesas
def ler_despesas():
    with open("despesas.pkl", "rb") as f:
        despesas = pickle.load(f)
    return despesas

# Criar o arquivo de despesas
criar_despesas()

# Ler e exibir as despesas
despesas = ler_despesas()
print("Despesas:")
for i, despesa in enumerate(despesas, 1):
    print(f"{i}. Dia: {despesa.dia}, Mês: {despesa.mes}, Categoria: {despesa.categoria}, Valor: {despesa.valor}, Descrição: {despesa.descricao}")
