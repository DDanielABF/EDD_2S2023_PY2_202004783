class Nodo_AVL():
    def __init__(self, valor,nombre, prioridad):
        self.valor = valor
        self.nombre = nombre
        self.prioridad = prioridad
        self.izquierdo = None
        self.derecho = None
        self.altura = 1
        self.factor_equilibrio = 0