import pickle
from dataclasses import dataclass

@dataclass
class RegItem:
    qtde: int
    unidade: str
    item: str

# Função para ler a lista de compras do arquivo binário
def ler_lista_compras(arquivo):
    with open(arquivo, 'rb') as infile:
        listadecompras = pickle.load(infile)
    return listadecompras

# Nome do arquivo onde a lista de compras está salva
nome_arquivo = input("Digite o nome do arquivo que deseja ler: ")

# Lendo a lista de compras do arquivo
lista_compras = ler_lista_compras(nome_arquivo)

# Exibindo a lista de compras
print("Lista de compras:")
for i, item in enumerate(lista_compras, 1):
    print(f"{i}. {item.item} - {item.qtde} {item.unidade}")
