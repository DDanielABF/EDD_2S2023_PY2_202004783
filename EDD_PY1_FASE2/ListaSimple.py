from NodoListaSimple import NodoListaSimple
class ListaSimple():
    def __init__(self):
        self.cabeza = None

    def agregar(self, idtarea,nombret,nombrep):
        nuevo_nodo = NodoListaSimple(idtarea,nombret,nombrep)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def proyectos(self):
        lista =[]
        actual =self.cabeza
        while actual:
            lista.append(actual.nombreT)
            actual=actual.siguiente
        return lista
    def imprimir(self):
        matriz=[]
        lista=[]
        actual = self.cabeza
        while actual:
            lista=[]
            lista.append(actual.idTarea)
            lista.append(actual.nombreT)
            lista.append(actual.nombreP)
            matriz.append(lista)
            print(actual.idTarea+"\n"+actual.nombreT+"\n"+actual.nombreP, end=" -> ")
            actual = actual.siguiente
        print("None")
        return matriz

    def imprimirP(self,nombrep):
        matriz=[]
        lista=[]
        actual = self.cabeza
        while actual:
            if actual.nombreT == nombrep:
                lista=[]
                lista.append(actual.idTarea)
                lista.append(actual.nombreT)
                lista.append(actual.nombreP)
                matriz.append(lista)
                print(actual.idTarea+"\n"+actual.nombreT+"\n"+actual.nombreP, end=" -> ")
            actual = actual.siguiente
        print("None")
        return matriz
  
    def eliminar(self):
        self.cabeza = None