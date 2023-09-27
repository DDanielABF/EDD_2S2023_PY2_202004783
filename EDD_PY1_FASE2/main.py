import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
import json
from arbolAVL import Arbol_AVL
from tablaHash import TablaHash
   
tablaGlobal = TablaHash()
arbol= Arbol_AVL()
def verificar_login():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()

    if usuario == "202004783" and contrasena == "admin":
        ventana_login.destroy() 
        abrir_ventana_principal()  
    elif tablaGlobal.buscar(usuario, contrasena):
        ventana_login.destroy()  
        abrir_ventana_empleados()  
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
    tabla = ttk.Treeview(ventana_principal, columns=("Columna1", "Columna2", "Columna3", "Columna4"))
    tabla.heading("#1", text="No.")
    tabla.heading("#2", text="Codigo Empleado")
    tabla.heading("#3", text="Nombre")
    tabla.heading("#4", text="Puesto")

    def AgregarTabla():
        tabla.delete(*tabla.get_children())
        for clave, valor in tablaGlobal.tabla.items():
            print(f"Clave: {clave}, Valor: {valor.codigo}")
            tabla.insert("", "end", values=(clave, valor.codigo, valor.nombre, valor.puesto))

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
                    id,nombre,password,puesto = fila #[FDEV-101,Cristian Suy,cris123,Frontend Developer]
                    tablaGlobal.Insertar(id,nombre,password,puesto)
            AgregarTabla()
    


    def cargar_json():
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
                        texto+=str(contenido_json['Proyectos'][i]['id'])+ '|'+ str(contenido_json['Proyectos'][i]['nombre'])
                               
                        
                        if len(contenido_json['Proyectos'][i]['tareas']) > 0:
                            for j in range(len(contenido_json['Proyectos'][i]['tareas'])):
                                texto+='\t'+'|'+str(contenido_json['Proyectos'][i]['tareas'][j]['nombre'])+ str(contenido_json['Proyectos'][i]['tareas'][j]['empleado']+'\n')
                        else:
                            texto+="\t"+"|No hay Tareas"+"\n"
                   
                   
                    print(texto)
                    texto_json.insert(tk.END, json.dumps(texto, indent=4))  # Mostrar el contenido JSON en la caja de texto
                    for i in range(len(contenido_json['Proyectos'])):
                        arbol.Insertar(contenido_json['Proyectos'][i]['id'],contenido_json['Proyectos'][i]['nombre'],contenido_json['Proyectos'][i]['prioridad'])
            
            except Exception as e:
                mensaje_error.config(text=f"Error: {str(e)}")

    def reporte_proyecto():
        arbol.graficar()

    def reporte_tarea():
        print("reporte tarea")

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
    boton_reporte2 = tk.Button(ventana_principal, text="reporte tareas",command=reporte_proyecto)
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
def abrir_ventana_empleados():
    ventana_principal = tk.Tk()
    ventana_principal.title("Empleados")
    ventana_principal.geometry("1280x800")
    ventana_principal.configure(bg="lightblue")
abrir_ventana_login()
