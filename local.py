import socket
import tkinter as tk
from tkinter import *
import shutil
from tkinter import filedialog
import os
from tkinter import simpledialog

LOCAL = r"C:/Users/jalex/Documents/ESCOM IPN/ESCOM 7TH SEM/REDES II/P1-SERVERDRIVE/LOCAL"
SERVER = r"C:/Users/jalex/Documents/ESCOM IPN/ESCOM 7TH SEM/REDES II/P1-SERVERDRIVE/SERVER"

# Dirección IP y puerto del servidor
HOST = '127.0.0.1'
PORT = 3312


def sel():
    main.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("all files","*.*"),("jpeg files","*.jpg")))
    print (main.filename)
    # main.destroy()
    return main.filename


def subirLOCAL():
    ruta = sel()
    if ruta:
        # Carpeta de destino en el servidor
        carpeta_destino = LOCAL

        # Obtener el nombre del archivo
        nombre_archivo = os.path.basename(ruta)

        try:
            # Copiar el archivo a la carpeta de destino
            shutil.copy2(ruta, os.path.join(carpeta_destino, nombre_archivo))
            print('Archivo subido exitosamente.')
        except IOError as e:
            print('No se pudo subir el archivo.')
            print(e)

def subirSERVER():
    ruta = sel()
    if ruta:
        # Carpeta de destino en el servidor
        carpeta_destino = SERVER

        # Obtener el nombre del archivo
        nombre_archivo = os.path.basename(ruta)

        try:
            # Copiar el archivo a la carpeta de destino
            shutil.copy2(ruta, os.path.join(carpeta_destino, nombre_archivo))
            print('Archivo subido exitosamente.')
        except IOError as e:
            print('No se pudo subir el archivo.')
            print(e)


def listar_archivos():
    # Establecer el directorio inicial
    initialdir = r"C:/Users/jalex/Documents/ESCOM IPN/ESCOM 7TH SEM/REDES II/P1-SERVERDRIVE/LOCAL"
    initialdir2 = r"C:/Users/jalex/Documents/ESCOM IPN/ESCOM 7TH SEM/REDES II/P1-SERVERDRIVE/SERVER"

    # Obtener la lista de archivos en el directorio
    archivos = os.listdir(initialdir)
    archivos2 = os.listdir(initialdir2)

    # Actualizar el Listbox con los nuevos archivos
    listbox.delete(0, tk.END)
    for archivo in archivos:
        listbox.insert(tk.END, archivo)

    listbox2.delete(0, tk.END)
    for archivo in archivos2:
        listbox2.insert(tk.END, archivo)

def refrescar_listbox():
    # Llamar a la función listar_archivos para refrescar el Listbox
    listar_archivos()

def renombrar_local():
    # Obtener el nombre del archivo seleccionado en la lista LOCAL
    nombre_archivo = listbox.get(tk.ACTIVE)
    # Obtener la ruta completa del archivo
    ruta_archivo = os.path.join(directorio, nombre_archivo)

    # Solicitar al usuario el nuevo nombre del archivo
    nuevo_nombre = simpledialog.askstring("Renombrar archivo", "Ingrese el nuevo nombre para el archivo:")
    if nuevo_nombre:
        # Construir la ruta completa del nuevo archivo
        ruta_nuevo_archivo = os.path.join(directorio, nuevo_nombre)

        try:
            # Renombrar el archivo
            os.rename(ruta_archivo, ruta_nuevo_archivo)
            print('Archivo renombrado:', nuevo_nombre)

            # Actualizar el Listbox para reflejar los cambios
            listar_archivos()

        except FileNotFoundError:
            print('Error: No se pudo encontrar el archivo especificado.')
        
        except OSError:
            print('Error: No se pudo renombrar el archivo.')

def renombrar_server():
    # Obtener el nombre del archivo seleccionado en la lista SERVER
    nombre_archivo = listbox2.get(tk.ACTIVE)
    # Obtener la ruta completa del archivo
    ruta_archivo = os.path.join(directorio2, nombre_archivo)

    # Solicitar al usuario el nuevo nombre del archivo
    nuevo_nombre = simpledialog.askstring("Renombrar archivo", "Ingrese el nuevo nombre para el archivo:")
    if nuevo_nombre:
        # Construir la ruta completa del nuevo archivo
        ruta_nuevo_archivo = os.path.join(directorio2, nuevo_nombre)

        try:
            # Renombrar el archivo
            os.rename(ruta_archivo, ruta_nuevo_archivo)
            print('Archivo renombrado:', nuevo_nombre)

            # Actualizar el Listbox para reflejar los cambios
            listar_archivos()

        except FileNotFoundError:
            print('Error: No se pudo encontrar el archivo especificado.')
        
        except OSError:
            print('Error: No se pudo renombrar el archivo.')

def eliminar_local():
    # Obtener el nombre del archivo seleccionado en la lista
    nombre_archivo = listbox.get(tk.ACTIVE)
    # Obtener la ruta completa del archivo
    ruta_archivo = os.path.join(directorio, nombre_archivo)

    try:
        # Eliminar el archivo
        os.remove(ruta_archivo)
        print('Archivo eliminado:', nombre_archivo)

        # Actualizar el Listbox para reflejar los cambios
        listar_archivos()

    except FileNotFoundError:
        print('Error: No se pudo encontrar el archivo especificado.')
    
    except OSError:
        print('Error: No se pudo eliminar el archivo.')

def eliminar_server():
    # Obtener el nombre del archivo seleccionado en la lista
    nombre_archivo = listbox2.get(tk.ACTIVE)
    # Obtener la ruta completa del archivo
    ruta_archivo = os.path.join(directorio2, nombre_archivo)

    try:
        # Eliminar el archivo
        os.remove(ruta_archivo)
        print('Archivo eliminado:', nombre_archivo)

        # Actualizar el Listbox para reflejar los cambios
        listar_archivos()

    except FileNotFoundError:
        print('Error: No se pudo encontrar el archivo especificado.')
    
    except OSError:
        print('Error: No se pudo eliminar el archivo.')

def crear_carpeta_local():
    # Solicitar al usuario el nombre de la carpeta
    nombre_carpeta = simpledialog.askstring("Crear carpeta", "Ingrese el nombre de la carpeta:")
    if nombre_carpeta:
        # Construir la ruta completa de la carpeta
        ruta_carpeta = os.path.join(directorio, nombre_carpeta)

        try:
            # Crear la carpeta
            os.mkdir(ruta_carpeta)
            print('Carpeta creada:', nombre_carpeta)

            # Actualizar el Listbox para reflejar los cambios
            listar_archivos()

        except FileExistsError:
            print('Error: La carpeta ya existe.')

def crear_carpeta_server():
    # Solicitar al usuario el nombre de la carpeta
    nombre_carpeta = simpledialog.askstring("Crear carpeta", "Ingrese el nombre de la carpeta:")
    if nombre_carpeta:
        # Construir la ruta completa de la carpeta
        ruta_carpeta = os.path.join(directorio2, nombre_carpeta)

        try:
            # Crear la carpeta
            os.mkdir(ruta_carpeta)
            print('Carpeta creada:', nombre_carpeta)

            # Actualizar el Listbox para reflejar los cambios
            listar_archivos()

        except FileExistsError:
            print('Error: La carpeta ya existe.')

def crear_archivo_local():
    # Solicitar al usuario el nombre del archivo
    nombre_archivo = simpledialog.askstring("Crear archivo", "Ingrese el nombre del archivo:")
    if nombre_archivo:
        # Construir la ruta completa del archivo
        ruta_archivo = os.path.join(directorio, nombre_archivo)

        try:
            # Crear el archivo
            open(ruta_archivo, 'a').close()
            print('Archivo creado:', nombre_archivo)

            # Actualizar el Listbox para reflejar los cambios
            listar_archivos()

        except FileExistsError:
            print('Error: El archivo ya existe.')

def crear_archivo_server():
    # Solicitar al usuario el nombre del archivo
    nombre_archivo = simpledialog.askstring("Crear archivo", "Ingrese el nombre del archivo:")
    if nombre_archivo:
        # Construir la ruta completa del archivo
        ruta_archivo = os.path.join(directorio2, nombre_archivo)

        try:
            # Crear el archivo
            open(ruta_archivo, 'a').close()
            print('Archivo creado:', nombre_archivo)

            # Actualizar el Listbox para reflejar los cambios
            listar_archivos()

        except FileExistsError:
            print('Error: El archivo ya existe.')

#creamos la funcion enviar para enviar un archivo mediante sockets
def enviar():
    #obtenemos el nombre del archivo seleccionado en la lista
    nombre_archivo = listbox.get(tk.ACTIVE)
    #obtenemos la ruta completa del archivo
    ruta_archivo = os.path.join(directorio, nombre_archivo)
    #obtenemos el tamaño del archivo
    tam = os.path.getsize(ruta_archivo)
    #creamos el socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #conectamos el socket
    s.connect((HOST, PORT))
    #enviamos el nombre del archivo
    s.send(nombre_archivo.encode())
    #recibimos el ok del server
    data = s.recv(1024)
    #enviamos el tamaño del archivo
    s.send(str(tam).encode())
    #recibimos el ok del server
    data = s.recv(1024)
    #abrimos el archivo en modo lectura binaria
    f = open(ruta_archivo, "rb")
    #leemos el archivo
    data = f.read()
    #enviamos el archivo
    s.sendall(data)
    #cerramos el archivo
    f.close()
    #cerramos el socket
    s.close()
    #imprimimos que se envio el archivo
    print("Archivo enviado")

def descargar():
    #obtenemos el nombre del archivo seleccionado en la lista
    nombre_archivo = listbox2.get(tk.ACTIVE)
    #obtenemos la ruta completa del archivo
    ruta = os.path.join(directorio2, nombre_archivo)
    
    if ruta:
        # Carpeta de destino en el servidor
        carpeta_destino = LOCAL

        # Obtener el nombre del archivo
        nombre_archivo = os.path.basename(ruta)

        try:
            # Copiar el archivo a la carpeta de destino
            shutil.copy2(ruta, os.path.join(carpeta_destino, nombre_archivo))
            print('Archivo descargado.')
        except IOError as e:
            print('No se pudo subir el archivo.')
            print(e)


#########################################################################################INICIO DE TKINTER##############################################################################################################

main = Tk()
main.title("DRIVE ALEX")
main.geometry("1000x600")

#label del primer listbox
label = Label(main, text="LOCAL", font=("Arial", 12))
label.grid(row=0, column=0)
#label del segundo listbox
label2 = Label(main, text="SERVER", font=("Arial", 12))
label2.grid(row=0, column=2)


directorio = r"C:/Users/jalex/Documents/ESCOM IPN/ESCOM 7TH SEM/REDES II/P1-SERVERDRIVE/LOCAL"
archivos = os.listdir(directorio)
listbox = Listbox(main,width=80)

# Agregar los nombres de archivos a la Listbox
for archivo in archivos:
    listbox.insert(tk.END, archivo)


directorio2 = r"C:/Users/jalex/Documents/ESCOM IPN/ESCOM 7TH SEM/REDES II/P1-SERVERDRIVE/SERVER"
archivos2 = os.listdir(directorio)
listbox2 = Listbox(main,width=80)

# Agregar los nombres de archivos a la Listbox
for archivo in archivos2:
    listbox2.insert(tk.END, archivo)

button = Button(main, text="SUBIR LOCAL", command=subirLOCAL)
button2 = Button(main, text="SUBIR SERVER", command=subirSERVER)
refrescar = Button(main, text="Refrescar", command=refrescar_listbox)
renombrar = Button(main, text="Renombrar", command=renombrar_local)
renombrar2 = Button(main, text="Renombrar", command=renombrar_server)
eliminar = Button(main, text="Eliminar", command=eliminar_local)
eliminar2 = Button(main, text="Eliminar", command=eliminar_server)
crear_carpeta = Button(main, text="Crear carpeta", command=crear_carpeta_local)
crear_carpeta2 = Button(main, text="Crear carpeta", command=crear_carpeta_server)
crear_archivo = Button(main, text="Crear archivo", command=crear_archivo_local)
crear_archivo2 = Button(main, text="Crear archivo", command=crear_archivo_server)
enviarservidor = Button(main, text="Enviar al servidor", command=enviar)
enviarserver = Button(main, text="Descargar Localmente", command=descargar)


hola = listar_archivos()

#listbox de la izquierda
listbox.grid(row=1, column=0)  # # #
#listbox de la derecha
listbox2.grid(row=1, column=2) #   #
#boton de refrescar
refrescar.grid(row=1, column=1)
#boton de subir local
button.grid(row=2, column=0)   #   #
#boton de subir server
button2.grid(row=2, column=2)
#boton de renombrar local
renombrar.grid(row=3, column=0)
#boton de renombrar server
renombrar2.grid(row=3, column=2)
#boton de eliminar local
eliminar.grid(row=4, column=0)
#boton de eliminar server
eliminar2.grid(row=4, column=2)
#boton de crear carpeta local
crear_carpeta.grid(row=5, column=0)
#boton de crear carpeta server
crear_carpeta2.grid(row=5, column=2)
#boton de crear archivo local
crear_archivo.grid(row=6, column=0)
#boton de crear archivo server
crear_archivo2.grid(row=6, column=2)
#boton de enviar al servidor
enviarservidor.grid(row=7, column=0)
#boton de enviar al server
enviarserver.grid(row=7, column=2)


main.mainloop()

#########################################################################################FINAL DE TKINTER##############################################################################################################
