import pickle
from dataclasses import dataclass

@dataclass
class RegItem:
    qtde: int
    unidade: str
    item: str

lista_compras = []

print("Qual nome deseja por no arquivo? (escreva '.pkl' depois do nome)")
nome_arquivo = input()

con = 1

print("Qual o " + str(con) + "° item deseja incluir? (digite '0' para terminar)")
item = input()

while item != '0':
    print("Qual a quantidade do item?")
    qtde = int(input())
    print("Qual a unidade do item?")
    unidade = input()
    lista_compras.append(RegItem(qtde=qtde, unidade=unidade, item=item))
    con += 1
    print("Qual o " + str(con) + "° item deseja incluir? (digite '0' para terminar)")
    item = input()

with open(nome_arquivo, 'wb') as outfile:
    pickle.dump(lista_compras, outfile)

print("Lista de compras salva com sucesso em", nome_arquivo)
