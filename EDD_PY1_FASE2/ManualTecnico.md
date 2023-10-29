# Manual Tecnico
## Introduccion
### se realizo la fase 2 del proyecto donde a continuacion se detallara que librerias,  estructuras se utilizaron con sus respectivas clases y funciones.
## Librerias
```python
import os
import csv
import json 
import tkinter
```
1. la libreria os se utilizo para poder abrir y escoger archivos desde la interfaz grafica
2. la libreria csv se utilizo para poder leer el archivo csv donde estaba la carga masiva
3. la libreria json se utilizo para poder leer el archivo json donde estaban los proyectos y tareas
4. la libreria tkinter se utilizo para poder realizar la interfaz grafica donde se realizo la fase 2 del proyecto

## Estructuras 
### Arbol AVL
##### Un árbol AVL es una estructura de datos de árbol de búsqueda binaria en la que la diferencia de alturas entre los subárboles izquierdo y derecho de cualquier nodo (conocida como el factor de equilibrio) está equilibrada o limitada, lo que garantiza un árbol balanceado.

#### Clases utilizadas en su implementacion
1.  arbolAVL.py
2. nodoAVL.py
### funciones utilizadas
``` python
class Arbol_AVL():
    def __init__(self):
        self.raiz = None
    
    def Insertar(self, valor, nombre, prioridad):
    def Altura(self, raiz):
    def Equilibrio(self, raiz):
    def RotacionI(self, raiz):
    def RotacionD(self, raiz):
    def InsertarNodo(self, valor,nombre,prioridad) 
    def graficar(self):
    def retornarValoresArbol(self, raiz, id):

```
1. la primera funcion llama a la funcion insertar nodo con los datos enviados del main

2. calcula la altura a la que se va a insertar
3. funcion recursiva que mira si hace rotacion derecha o izquierda
4. realiza la rotacion hacia la izquierda
5. realiza la rotacion hacia la derecha
6. despues de pasar por todo el proceso de insercion se guarda al nodo
7. en esta se realiza el reporte grafico con graphviz
8. sirve para poder adjuntar los valores del arbol al reporte de graphviz.
### Arbol B
##### Un árbol B es una estructura de datos de árbol generalizada que puede tener múltiples claves en cada nodo y múltiples hijos, diseñado para manejar grandes conjuntos de datos y permitir una alta eficiencia en operaciones de búsqueda, inserción y eliminación.
### Clases utilizadas en su implementacion
1.  arbolB.py
2. nodoB.py
3. ramaB.py
### funciones utilizadas
```python


    def insertar(self, valor,nombre,idencargado)    
    def insertar_rama(self, nodo:NodoB, rama:RamaB):
    def dividir(self, rama:RamaB):
    def suma_ascii(self, cadena):
    def graficar(self):
    def Grafo(self, rama:NodoB):
    def GrafoRamas(self, rama:NodoB):
    def conexionRamas(self, rama:NodoB):
    def Buscar(self,idencargado):
    def GrafoBuscar(self, rama:NodoB,idencargado, lista:ListaSimple):
    def GrafoRamasBuscar(self, rama:NodoB,idencargado, lista:ListaSimple):
```
1. trae los dato desde el main para insertarlos al nodo


2. se inserta la rama a la que se incluira el nodo insertado
3. divide las ramas existentes con las nuevas
4. realiza la operacion para sacar el valor del nodo
5. crea el inicio del reporte graphviz
6. grafica los nodos
7. realiza las conexiones para ordenar los nodos
8. trae el dato de idencargado desde el main para poder realizar la busqueda
9. decide si busca por la izquierda o derecha
10. verifica si el nodo encontrado coincide para poder guardarlo en una lista simple
### Tabla hash
##### Una tabla hash es una estructura de datos que se utiliza para almacenar y recuperar datos en función de una clave. Está diseñada para proporcionar acceso rápido a los datos y es eficiente en términos de tiempo de búsqueda.
### Clases utilizadas en su implementacion
1.  tablaHash.py
2. nodoHash.py
### funciones utilizadas
```python
class TablaHash():
    def __init__(self) -> None:
    def Insertar(self, codigo, nombre, password, puesto):
    def calculoIndice(self, codigo):
    def capacidadTabla(self):
    def nuevaCapacidad(self):
    def reInsertar(self):
    def reCalculoIndice(self, codigo, intento):
    def nuevoIndice(self, nuevoIndice):
    def buscar(self, codigo, password):
```
1. adquiere los datos del login del main
2. calcula el indice actual ya que cambia dependiendo el espacio
3. verifica si se necesita crear mas capacidad o no 
4. reinserta el nodo a la tabla despues de las verificaciones anteriores
5. vuelve a calcular el indice luego de reinsertar el nodo
6. crea un nuevo indice de ser necesaio
7. verifica si el usuario y clave ingresados en el login son validos o estan en la tabla hash
### Lista simplemente enlazada
##### Una lista simple es una estructura de datos lineal que consta de nodos enlazados secuencialmente, donde cada nodo contiene datos y una referencia (o enlace) al siguiente nodo en la secuencia.
1.  ListaSimple.py
2. NodoListaSimple.py
### funciones utilizadas
```python
    def agregar(self, idtarea,nombret,nombrep):
    def proyectos(self):
    def imprimir(self):
    def eliminar(self)
```
1. agrega el nodo lista simple desde el recorrido del arbol b
2. retorna los proyectos del empleado en funcion
3. imprime los datos de las tareas del empleado segun el proyecto indicado
4. elimina la lista
## main
### funciones
```python
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
import json
from arbolAVL import Arbol_AVL
from tablaHash import TablaHash
from arbolB import ArbolB
from ListaSimple import ListaSimple
tablaGlobal = TablaHash()
arbol= Arbol_AVL()
arbolB = ArbolB() 
listaS = ListaSimple()
def verificar_login():
def abrir_ventana_principal():
    def AgregarTabla():
    def leer_csv():
    def cargar_json():
    def reporte_proyecto():   
    def reporte_tarea():
def abrir_ventana_login():
def abrir_ventana_empleados(idenc):
    def AgregarTabla():
        
    
abrir_ventana_login()
```

1. crea la venta a travez de tkinter para poder realizar el login del admin y de empleados
2. crea la ventana del administrador
   - agrega los datos del csv a la tabla de la interfaz y a la estructura hash
   - agrega los datos del archivo json al cuadro de texto y a los arboles anteriormente indicados
   - 
3. vuelve a abrir el login luego de cerrar sesion
4. abre la ventana de los empleados a traves de tkinter y muestra las tareas y sus respectivos proyectos
   - agrega la tabla de cada tarea de los proyectos asignados del empleado

## Conclusion
### Project Up Fase 2 es una aplicacion de escritorio con interfaz grafica que se dedica a insertar datos de distintos tipos de archivo hacia estructuras avanzadas de datos para poder usar su optimizacion y eficiencia a favor y poder visualizarlos de la mejor manera.