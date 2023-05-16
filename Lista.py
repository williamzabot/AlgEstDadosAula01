
from No import No

class Lista:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def add(self, valor):
        no = No(valor)
        if self.inicio is not None:
            no.proximo = self.inicio
        self.inicio = no
        self.tamanho += 1

    def addFim(self, valor):
        no = No(valor)
        if self.inicio is None:
            self.inicio = no
        else:
            aux = self.inicio
            while aux.proximo:
                aux = aux.proximo
            aux.proximo = no
        self.tamanho += 1

    def imprimir(self):
        if self.inicio is None:
            print("lista vazia")
        else:
            aux = self.inicio
            while aux:
                print(aux.dado)
                aux = aux.proximo

    def removerInicio(self):
        if self.inicio is None:
            print("lista vazia")
        else:
            self.inicio = self.inicio.proximo
            self.tamanho -= 1

    def removerFim(self):
        if self.inicio is None:
            print("lista vazia")
        else:
            anterior = self.inicio
            aux = self.inicio.proximo
            while aux.proximo:
                anterior = aux
                aux = aux.proximo
            anterior.proximo = None
            aux.proximo = None
            self.tamanho -= 1





lista = Lista()
lista.addFim("William")
lista.addFim("José")
lista.addFim("Marcos")
lista.removerFim()
lista.imprimir()
