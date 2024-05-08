import json

lista_compras = []

print("Qual nome deseja por no arquivo? (escreva '.json' depois do nome)")
listaCompras = input()

con = 1

print("Qual o " + str(con) + "° item deseja incluir? (escreva 'fim' se quiser terminar)")
item = input()

while item != "fim":
    print("Qual a quantidade do item?")
    qtde = int(input())
    lista_compras.append({"item": item, "quantidade": qtde})
    con += 1
    print("Qual o " + str(con) + "° item deseja incluir? (escreva 'fim' se quiser terminar)")
    item = input()

with open(listaCompras, 'w') as outfile:
    json.dump(lista_compras, outfile)

print("Lista de compras salva com sucesso em", listaCompras)
