from nodoHash import NodoHash

class TablaHash():
    def __init__(self) -> None:
        self.tabla = {} 
        self.capacidad = 5 #8
        self.utilizacion = 0 #0

    def Insertar(self, codigo, nombre, password, puesto):
        indice = self.calculoIndice(codigo)
        nuevo = NodoHash(codigo, nombre, password, puesto)
        if indice < self.capacidad:
            try:
                if not (indice in self.tabla):
                    self.tabla[indice] = nuevo
                    self.utilizacion += 1
                    self.capacidadTabla()
                else:
                    contador = 1
                    indice = self.reCalculoIndice(codigo, contador)
                    while (indice in self.tabla):
                        contador += 1
                        indice = self.reCalculoIndice(codigo, contador)
                    self.tabla[indice] = nuevo
                    self.utilizacion += 1
                    self.capacidadTabla()
            except:
                print("Error!!!!")

    def calculoIndice(self, codigo):
        total = 0
        for caracter in codigo:
            valor_ascii = ord(caracter)
            total += valor_ascii
        indice = total % self.capacidad
        return indice
    
    def capacidadTabla(self):
        capacidadActual = self.capacidad*0.70 # 8 * 0.70= 6 {0,1,2,3,4..,6}
        if self.utilizacion > capacidadActual: # 0 > 5
            self.capacidad = self.nuevaCapacidad()
            self.utilizacion = 0
            self.reInsertar()

    def nuevaCapacidad(self):
        cont = 0
        a, b = 0, 1 #0, 1, 1, 2, 3, 5, 8, 13, 21, 34....
        while cont < 15:
            cont += 1
            if a > self.capacidad:
                return a
            a, b = b, a + b
        return a

    def reInsertar(self):
        tablaAux = self.tabla
        self.tabla = {}
        for _, valor in tablaAux.items():
            self.Insertar(valor.codigo, valor.nombre, valor.password, valor.puesto)

    def reCalculoIndice(self, codigo, intento):
        nuevoIndice = self.calculoIndice(codigo) + (intento*intento) #2 + (2*2) = 6
        return self.nuevoIndice(nuevoIndice)
    
    def nuevoIndice(self, nuevoIndice):
        nuevaPosicion = 0
        if nuevoIndice < self.capacidad:
            nuevaPosicion = nuevoIndice
        else:
            nuevaPosicion = nuevoIndice - self.capacidad
            nuevaPosicion = self.nuevoIndice(nuevaPosicion)
        return nuevaPosicion
    
    def buscar(self, codigo, password):
        indice = self.calculoIndice(codigo)
        #for i in self.tabla:
           # print(self.tabla[i].)
        if indice < self.capacidad:
            try:
                if (indice in self.tabla):
                    empleado =  self.tabla[indice]
                    print(empleado.codigo)
                    if empleado.codigo == codigo and empleado.password == password:
                        return True
                    else:
                        contador = 1
                        indice = self.reCalculoIndice(codigo, contador)
                        while not (indice in self.tabla):
                            contador += 1
                            indice = self.reCalculoIndice(codigo, contador)
                            empleado =  self.tabla[indice]
                            if empleado.codigo == codigo and empleado.password == password:
                                return True
                        
                elif not (indice in self.tabla):
                    return False
                else:
                    contador = 1
                    indice = self.reCalculoIndice(codigo, contador)
                    while not (indice in self.tabla):
                        contador += 1
                        indice = self.reCalculoIndice(codigo, contador)
                        empleado =  self.tabla[indice]
                        if empleado.codigo == codigo and empleado.password == password:
                            return True
            except:
                print("Error")
        return False
    def buscarMejorado(self, codigo, password):
        indice = self.calculoIndice(codigo)
    
        if indice < self.capacidad:
            try:
                if indice in self.tabla:
                    empleado = self.tabla[indice]
                    if empleado.codigo == codigo and empleado.password == password:
                        return True
                    else:
                        contador = 1
                        indice = self.reCalculoIndice(codigo, contador)
                        while indice  in self.tabla:
                            empleado = self.tabla[indice]
                            if empleado.codigo == codigo and empleado.password == password:
                                return True
                            contador += 1
                            indice = self.reCalculoIndice(codigo, contador)
                else:
                    contador = 1
                    indice = self.reCalculoIndice(codigo, contador)
                    while indice  in self.tabla:
                        empleado = self.tabla[indice]
                        if empleado.codigo == codigo and empleado.password == password:
                            return True
                        contador += 1
                        indice = self.reCalculoIndice(codigo, contador)
                        
            except:
                print("Error")
    
        return False
#En esta versión, se elimina el elif y el manejo de que el índice no esté en self.tabla se coloca directamente en el bloque else. Esto debería solucionar el problema y permitir que la lógica funcione correctamente.





