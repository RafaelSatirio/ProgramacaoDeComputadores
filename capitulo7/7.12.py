import pickle

class Despesa:
    def __init__(self, dia, mes, categoria, valor, descricao):
        self.dia = dia
        self.mes = mes
        self.categoria = categoria
        self.valor = valor
        self.descricao = descricao

# Dicionário de categorias
categorias = {
    1: "Despesas fixas",
    2: "Transporte",
    3: "Alimentação",
    4: "Lazer",
    5: "Saúde"
}

# Dicionário de meses
meses = {
    1: "Jan",
    2: "Fev",
    3: "Mar",
    4: "Abr",
    5: "Mai",
    6: "Jun",
    7: "Jul",
    8: "Ago",
    9: "Set",
    10: "Out",
    11: "Nov",
    12: "Dez"
}

# Função para ler o arquivo de despesas
def ler_despesas():
    with open("despesas.pkl", "rb") as f:
        despesas = pickle.load(f)
    return despesas

# Ler e exibir as despesas
despesas = ler_despesas()
print("Despesas:")
print("{:<10} {:<15} {:<10} {:<20}".format("Data", "Categoria", "Valor", "Descrição"))

# Dicionário para armazenar o total de despesas por categoria
total_por_categoria = {categoria: 0 for categoria in categorias.values()}

for despesa in despesas:
    categoria = categorias.get(despesa.categoria, "Categoria inválida")
    mes = meses.get(despesa.mes, "Mês inválido")
    data = f"{despesa.dia:02d}/{mes}"
    valor_formatado = f"R${despesa.valor:.2f}"
    print("{:<10} {:<15} {:<10} {:<20}".format(data, categoria, valor_formatado, despesa.descricao))
    
    # Atualizar o total de despesas para a categoria
    total_por_categoria[categoria] += despesa.valor

# Exibir o resumo das despesas por categoria
print("\nResumo das despesas por categoria:")
for categoria, total in total_por_categoria.items():
    print(f"{categoria}: R${total:.2f}")
