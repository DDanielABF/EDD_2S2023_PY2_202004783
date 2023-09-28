from NodoListaSimple import NodoListaSimple
class ListaSimple():
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo_nodo = NodoListaSimple(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

    def eliminar(self):
        self.cabeza = None