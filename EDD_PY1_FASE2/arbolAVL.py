from nodoAVL import Nodo_AVL
import os

class Arbol_AVL():
    def __init__(self):
        self.raiz = None
    
    def Insertar(self, valor, nombre, prioridad):
        self.raiz = self.InsertarNodo(valor,nombre,prioridad, self.raiz)

    def Altura(self, raiz):
        condicion = raiz == None
        return 0 if condicion else raiz.altura
    
    def Equilibrio(self, raiz):
        condicion = raiz == None
        return 0 if condicion else (self.Altura(raiz.derecho) - self.Altura(raiz.izquierdo))

    def RotacionI(self, raiz):
        raiz_derecho = raiz.derecho
        hijo_izquierdo = raiz_derecho.izquierdo
        raiz_derecho.izquierdo = raiz
        raiz.derecho = hijo_izquierdo
        raiz.altura = 1 + max(self.Altura(raiz.izquierdo),self.Altura(raiz.derecho))
        raiz.factor_equilibrio = self.Equilibrio(raiz)
        raiz_derecho.altura = 1 + max(self.Altura(raiz_derecho.izquierdo),self.Altura(raiz_derecho.derecho))
        raiz_derecho.factor_equilibrio = self.Equilibrio(raiz_derecho)
        return raiz_derecho
    
    def RotacionD(self, raiz):
        raiz_izquierdo = raiz.izquierdo
        hijo_derecho = raiz_izquierdo.derecho
        raiz_izquierdo.derecho = raiz
        raiz.izquierdo = hijo_derecho
        raiz.altura = 1 + max(self.Altura(raiz.izquierdo), self.Altura(raiz.derecho))
        raiz.factor_equilibrio = self.Equilibrio(raiz)
        raiz_izquierdo.altura = 1 + max(self.Altura(raiz_izquierdo.izquierdo), self.Altura(raiz_izquierdo.derecho))
        raiz_izquierdo.factor_equilibrio = self.Equilibrio(raiz_izquierdo)
        return raiz_izquierdo

    def InsertarNodo(self, valor,nombre,prioridad, raiz):
        if raiz is None:
            return Nodo_AVL(valor,nombre,prioridad)
        else:
            if raiz.valor == valor:
                raiz.valor = valor
                raiz.nombre = nombre
                raiz.prioridad = prioridad
            elif raiz.valor > valor:
                raiz.izquierdo = self.InsertarNodo(valor,nombre,prioridad, raiz.izquierdo)
            elif raiz.valor < valor:
                raiz.derecho = self.InsertarNodo(valor,nombre,prioridad, raiz.derecho)
        #Luego de insercion, procedemos a realizar rotaciones
        raiz.altura = 1 + max(self.Altura(raiz.izquierdo),self.Altura(raiz.derecho))
        balanceo = self.Equilibrio(raiz)
        raiz.factor_equilibrio = balanceo

        if balanceo > 1 and valor > raiz.derecho.valor:#Rotacion Simple a la Izquierda
            return self.RotacionI(raiz)
        if balanceo < -1 and valor < raiz.izquierdo.valor:#Rotacion Simple a la Derecha
            return self.RotacionD(raiz)
        if balanceo > 1 and valor < raiz.derecho.valor:#Rotacion Doble a la Izquierda
            raiz.derecho = self.RotacionD(raiz.derecho)
            return self.RotacionI(raiz)
        if balanceo < -1 and valor > raiz.izquierdo.valor:#Rotacion Doble a la Derecha
            raiz.izquierdo = self.RotacionI(raiz.izquierdo)
            return self.RotacionD(raiz)
        return raiz
    
    def recorridoInorden(self):
        self.Inorden(self.raiz)

    def Inorden(self, raiz):
        if raiz is not None:
            self.Inorden(raiz.izquierdo)
            print(raiz.valor, end=' ')
            self.Inorden(raiz.derecho)

    def recorridoPreOrden(self):
        self.PreOrden(self.raiz)
    
    def PreOrden(self, raiz):
        if raiz is not None:
            print(raiz.valor, end=' ')
            self.PreOrden(raiz.izquierdo)
            self.PreOrden(raiz.derecho)

    def recorridoPostOrden(self):
        self.PostOrden(self.raiz)

    def PostOrden(self, raiz):
        if raiz is not None:
            self.PostOrden(raiz.izquierdo)
            self.PostOrden(raiz.derecho)
            print(raiz.valor, end=' ')

    def graficar(self):
        cadena = ''
        archivo = "arbolAVL.jpg"
        a = open("arbolAVL.dot","w")
        if self.raiz is not None:
            cadena += "digraph arbolAVL {"
            cadena += self.retornarValoresArbol(self.raiz, 0)
            cadena += "}"
        a.write(cadena)
        a.close()
        os.system("dot -Tjpg arbolAVL.dot -o " + archivo)
        #os.system(archivo)


    def retornarValoresArbol(self, raiz, id):
        cadena = ''
        numero = id + 1
        if raiz is not None:
            cadena += "\""
            cadena += "id:{}\nnombre:{}\nnivel:{}".format(raiz.valor,raiz.nombre,raiz.altura)
            cadena += "\" ;\n"
            if(raiz.izquierdo is not None and raiz.derecho is not None):
                cadena += "x{} [label=\"\",width=.1,style=invis];\n".format(numero)
                cadena += "\"id:{}\nnombre:{}\nnivel:{}\" -> {} \"id:{}\nnombre:{}\nnivel:{}\" -> {}".format(raiz.valor,raiz.nombre,raiz.altura, self.retornarValoresArbol(raiz.izquierdo, numero), raiz.valor, raiz.nombre,raiz.altura,self.retornarValoresArbol(raiz.derecho, numero))
                cadena += "{" + "rank=same" + "\"id:{}\nnombre:{}\nnivel:{}\" -> \"id:{}\nnombre:{}\nnivel:{}\" [style=invis]; ".format(raiz.izquierdo.valor,raiz.izquierdo.nombre,raiz.izquierdo.altura, raiz.derecho.valor,raiz.derecho.nombre, raiz.derecho.altura) + "} \n"
            elif(raiz.izquierdo is not None and raiz.derecho is None):
                cadena += "x{} [label=\"\",width=.1,style=invis];\n".format(numero)
                cadena += "\"id:{}\nnombre:{}\nnivel:{}\" -> {} \"id:{}\nnombre:{}\nnivel:{}\" -> x{}[style=invis];\n".format(raiz.valor,raiz.nombre,raiz.altura, self.retornarValoresArbol(raiz.izquierdo, numero), raiz.valor,raiz.nombre,raiz.prioridad, numero)
                cadena += "{" + "rank=same " + "\"id:{}\nnombre:{}\nnivel:{}\" -> x{} [style=invis]; ".format(raiz.izquierdo.valor,raiz.izquierdo.nombre,raiz.izquierdo.altura, numero) + "} \n"
            elif(raiz.izquierdo is None and raiz.derecho is not None):
                cadena += "x{} [label=\"\",width=.1,style=invis];\n".format(numero)
                cadena += "\"id:{}\nnombre:{}\nnivel:{}\" -> x{}[style=invis]; \n \"id:{}\nnombre:{}\nnivel:{}\" -> {}".format(raiz.valor,raiz.nombre,raiz.altura, numero, raiz.valor,raiz.nombre,raiz.prioridad, self.retornarValoresArbol(raiz.derecho, numero))
                cadena += "{" + "rank=same " + "x{} -> \"id:{}\nnombre:{}\nnivel:{}\" [style=invis]; ".format(numero, raiz.derecho.valor,raiz.derecho.nombre,raiz.derecho.altura) + "} \n"
        return cadena