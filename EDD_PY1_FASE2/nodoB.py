class NodoB():
    def __init__(self, valor, id,nombre,idencargado,idproyecto): #Valor sera el numero final del ascii, y id sera el id de la tarea
        self.valor = valor
        self.id = id
        self.idencargado= idencargado
        self.idproyecto = idproyecto
        self.nombre = nombre
        self.siguiente = None
        self.anterior = None
        self.izquierda = None
        self.derecha = None