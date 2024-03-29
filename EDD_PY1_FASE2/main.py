import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
import json
import hashlib
from arbolAVL import Arbol_AVL
from tablaHash import TablaHash
from arbolB import ArbolB
from ListaSimple import ListaSimple
tablaGlobal = TablaHash()
arbol= Arbol_AVL()
arbolB = ArbolB() 
listaS = ListaSimple()

def sha256(text):
  """
  Encripta una cadena de texto utilizando el método de encriptación SHA-256.

  Args:
    text: La cadena de texto a encriptar.
    salt: La sal a utilizar.

  Returns:
    La cadena encriptada.
  """

  hash_object = hashlib.sha256()
  hash_object.update((text).encode())
  return hash_object.hexdigest()
def verificar_login():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()

    if usuario == "202004783" and contrasena == "admin":
        ventana_login.destroy() 
        abrir_ventana_principal()  
    elif tablaGlobal.buscarMejorado(usuario, sha256(contrasena)):
        ventana_login.destroy()  
        abrir_ventana_empleados(usuario)  
    else:
        messagebox.showerror("Error de inicio de sesión", "Credenciales incorrectas")

def abrir_ventana_principal():
    ventana_principal = tk.Tk()
    ventana_principal.title("ADMINISTRADOR")
    ventana_principal.geometry("1280x800")
    ventana_principal.configure(bg="lightblue")
    etiqueta_identificacion = tk.Label(ventana_principal, text="Project Manager")
    etiqueta_identificacion.pack(pady=2)
    etiqueta_identificacion = tk.Label(ventana_principal, text="202004783-Daniel Barrera")
    etiqueta_identificacion.pack(side=tk.RIGHT, padx=10, pady=5)
    tabla = ttk.Treeview(ventana_principal, columns=("Columna1", "Columna2", "Columna3","Columna4", "Columna5"))
    tabla.heading("#1", text="No.")
    tabla.heading("#2", text="Codigo Empleado")
    tabla.heading("#3", text="password")
    tabla.heading("#3", text="Nombre")
    tabla.heading("#4", text="Puesto")

    def AgregarTabla():
        tabla.delete(*tabla.get_children())
        
        for clave, valor in tablaGlobal.tabla.items():
            print(f"Clave: {clave}, Valor: {valor.codigo}")
            tabla.insert("", "end", values=(clave, valor.codigo,valor.password, valor.nombre, valor.puesto))

    if tablaGlobal.utilizacion > 0:
        AgregarTabla()

    def leer_csv():
        ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])

        if ruta_archivo:
            tabla.delete(*tabla.get_children()) 

            with open(ruta_archivo, newline="\n") as archivo_csv:
                lector_csv = csv.reader(archivo_csv)
                next(lector_csv) 

                for fila in lector_csv:
                    id,nombre,password,puesto = fila 
                    tablaGlobal.Insertar(id,nombre,sha256(password),puesto)
            AgregarTabla()
    


    def cargar_json():
        lineas=[]
    # Abrir un cuadro de diálogo para seleccionar el archivo JSON
        archivo = filedialog.askopenfilename(filetypes=[("Archivos JSON", "*.json")])
        texto=""
        if archivo:
            try:
            # Leer y cargar el contenido del archivo JSON
                with open(archivo, "r") as file:
                    contenido_json = json.load(file)
                    texto_json.delete("1.0", tk.END)  # Limpiar el contenido anterior en la caja de texto
                    for i in range(len(contenido_json['Proyectos'])):
                        arbol.Insertar(contenido_json['Proyectos'][i]['id'],contenido_json['Proyectos'][i]['nombre'],contenido_json['Proyectos'][i]['prioridad'])
                    
                    
                    
                    for i in range(len(contenido_json['Proyectos'])):
                        texto+=str(contenido_json['Proyectos'][i]['id'])+ '|'+ str(contenido_json['Proyectos'][i]['nombre'])
                        lineas.append(str(contenido_json['Proyectos'][i]['id'])+ '|'+ str(contenido_json['Proyectos'][i]['nombre']))     
                        
                        if len(contenido_json['Proyectos'][i]['tareas']) > 0:
                            for j in range(len(contenido_json['Proyectos'][i]['tareas'])):
                                texto+='    '+'|'+str(contenido_json['Proyectos'][i]['tareas'][j]['nombre'])+ str(contenido_json['Proyectos'][i]['tareas'][j]['empleado']+'\n')
                                lineas.append('    '+'|'+str(contenido_json['Proyectos'][i]['tareas'][j]['nombre'])+ str(contenido_json['Proyectos'][i]['tareas'][j]['empleado']+'\n'))
                        else:
                            texto+="    "+"|No hay Tareas"+"\n"
                            lineas.append("    "+"|No hay Tareas"+"\n")

                    txt=""
                    for i in range(len(lineas)):
                        txt+=lineas[i]
                    texto_json.insert(tk.END, json.dumps(lineas, indent=4))  # Mostrar el contenido JSON en la caja de texto
                    for i in range(len(contenido_json['Proyectos'])):
                            
                        
                        if len(contenido_json['Proyectos'][i]['tareas']) > 0:
                            id=0
                            for j in range(len(contenido_json['Proyectos'][i]['tareas'])):
                                id+=1
                                idt="T"+str(id)+"-"+str(contenido_json['Proyectos'][i]['id'])
                                nombre=str(contenido_json['Proyectos'][i]['tareas'][j]['nombre'])
                                encargado = str(contenido_json['Proyectos'][i]['tareas'][j]['empleado'])
                                proyecto=str(contenido_json['Proyectos'][i]['id'])
                                #texto+='\t'+'|'+str(contenido_json['Proyectos'][i]['tareas'][j]['nombre'])+ str(contenido_json['Proyectos'][i]['tareas'][j]['empleado']+'\n')
                                #print(idt)
                                
                                arbolB.insertar(idt,nombre,encargado,proyecto)
                                
                        
                        else:
                            print("proyecto vacio")
                    
                    
                    
           
           
            except Exception as e:
                mensaje_error.config(text=f"Error: {str(e)}")
                print(e)

    def reporte_proyecto():
        arbol.graficar()

    def reporte_tarea():
        arbolB.graficar()

# Etiqueta para mostrar mensajes de error
    mensaje_error = tk.Label(ventana_principal, text="", fg="red")
    mensaje_error.pack(pady=5)


    #boton_leer_csv = tk.Button(ventana_principal, text="Leer CSV", command=leer_csv)
    #boton_leer_csv.pack(pady=20)

    tabla.pack(pady=15)
    boton_leer_json = tk.Button(ventana_principal, text="Leer CSV", command=leer_csv)
    boton_leer_json.pack(pady=15)
    def cerrar_sesion():
        ventana_principal.destroy()
        abrir_ventana_login()
# Caja de texto para mostrar el contenido JSON
    texto_json = tk.Text(ventana_principal, wrap=tk.WORD, width=70, height=10)
    texto_json.pack()

# Botón para cargar el archivo JSON
    boton_cargar = tk.Button(ventana_principal, text="Cargar Archivo JSON", command=cargar_json)
    boton_cargar.pack(pady=15)
#botones de reportes
    boton_reporte = tk.Button(ventana_principal, text="reporte proyectos",command=reporte_proyecto)
    boton_reporte.pack(side=tk.LEFT, padx=20)
    boton_reporte2 = tk.Button(ventana_principal, text="reporte tareas",command=reporte_tarea)
    boton_reporte2.pack(side=tk.LEFT, padx=20)
    boton_cerrar_sesion = tk.Button(ventana_principal, text="Cerrar Sesión", command=cerrar_sesion)
    boton_cerrar_sesion.pack(side=tk.RIGHT, padx=20)

    ventana_principal.mainloop()

def abrir_ventana_login():
    global ventana_login, entry_usuario, entry_contrasena
    ventana_login = tk.Tk()
    ventana_login.title("ProjectUp")
    ventana_login.geometry("400x450") 
    #imagen = tk.PhotoImage(file="unnamed.png")

    label_imagen = ttk.Label(ventana_login)
    label_imagen.pack(pady=20)
    label_portada = tk.Label(ventana_login, text="INICIO DE SESION\nProjectUp")
    label_portada.pack(pady=20)

    label_usuario = tk.Label(ventana_login, text="Usuario:")
    label_contrasena = tk.Label(ventana_login, text="Contraseña:")
    entry_usuario = tk.Entry(ventana_login)
    entry_contrasena = tk.Entry(ventana_login, show="*")  

    label_usuario.pack()
    entry_usuario.pack()
    label_contrasena.pack()
    entry_contrasena.pack()

    boton_ingresar = tk.Button(ventana_login, text="Ingresar", command=verificar_login)
    boton_ingresar.pack(pady=20)

    label_pie = tk.Label(ventana_login, text="fase 2 - project up")
    label_pie.pack(pady=20)

    ventana_login.mainloop()
def abrir_ventana_empleados(idenc):
    #listaS.eliminar()
    lista=[]
    listaS = arbolB.Buscar(idenc)
    
    ventana_principal = tk.Tk()
    ventana_principal.title("Empleados")
    ventana_principal.geometry("1280x800")
    ventana_principal.configure(bg="yellow")
    etiqueta_identificacion = tk.Label(ventana_principal, text=idenc)
    etiqueta_identificacion.pack(side=tk.RIGHT, padx=10, pady=5)
    matriz=[]
    Proyectos=[]
    matriz = listaS.imprimir()
    proyectos = listaS.proyectos()
    def AgregarTablap(event):
        print(combo_proyectos.get())
        matrix=[]
        nombrep = combo_proyectos.get()
        matrix = listaS.imprimirP(nombrep)
        tabla.delete(*tabla.get_children())
        
        for i in range(len(matrix)):
            
            
            tabla.insert("", "end", values=( matrix[i][0], matrix[i][1], matrix[i][2]))
    #proyectos = ["Proyecto 1", "Proyecto 2", "Proyecto 3", "Proyecto 4", "Proyecto 5"]
    combo_proyectos = ttk.Combobox(ventana_principal, values=proyectos)
    
    combo_proyectos.pack(pady=20)
    tabla = ttk.Treeview(ventana_principal, columns=("Columna1", "Columna2", "Columna3"))
    tabla.heading("#1", text="Codigo de Tarea")
    tabla.heading("#2", text="Nombre de Proyecto")
    tabla.heading("#3", text="Nombre de la Tarea")
    

   
        
            

    def AgregarTabla():
        for i in range(len(matriz)):
            
            
            tabla.insert("", "end", values=( matriz[i][0], matriz[i][1], matriz[i][2]))
    AgregarTabla()
    combo_proyectos.bind("<<ComboboxSelected>>",AgregarTablap)
    

    tabla.pack(pady=15)
    def cerrar_sesion():
        ventana_principal.destroy()
        abrir_ventana_login()
    boton_cerrar_sesion = tk.Button(ventana_principal, text="Cerrar Sesión", command=cerrar_sesion)
    boton_cerrar_sesion.pack(side=tk.RIGHT, padx=20)
    ventana_principal.mainloop()
abrir_ventana_login()
