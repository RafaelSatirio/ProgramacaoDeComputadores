class No:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def insere(self, novo, antecessor=None):
        novo_no = No(novo)
        
        if antecessor is None:
            # Inserção no início da lista
            novo_no.prox = self.cabeca
            self.cabeca = novo_no
        else:
            # Procurar o antecessor
            atual = self.cabeca
            while atual is not None and atual.dado != antecessor:
                atual = atual.prox

            if atual is None:
                print("Antecessor não encontrado na lista.")
                return

            # Inserir novo nó após o antecessor
            novo_no.prox = atual.prox
            atual.prox = novo_no

    def imprimir_lista(self):
        atual = self.cabeca
        while atual is not None:
            print(atual.dado, end=" -> ")
            atual = atual.prox
        print("None")

# Exemplo de uso
lista = ListaEncadeada()
lista.insere(3)
lista.insere(5, 3)
lista.insere(2)
lista.insere(4, 5)
lista.imprimir_lista()
