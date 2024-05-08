import json

# Nome do arquivo onde a lista de compras está salva
lista_compras_arquivo = "listadecompras.json"

# Função para ler a lista de compras do arquivo JSON
def ler_lista_compras(arquivo):
    with open(arquivo, 'r') as infile:
        lista_compras = json.load(infile)
    return lista_compras

# Lendo a lista de compras do arquivo
lista_compras = ler_lista_compras(lista_compras_arquivo)

# Exibindo a lista de compras
print("Lista de compras:")
for i, item in enumerate(lista_compras, 1):
    quantidade = item.get('quantidade', '')
    unidade = item.get('unidade', '')
    print(f"{i}. {item['item']} - {unidade} {quantidade}")
