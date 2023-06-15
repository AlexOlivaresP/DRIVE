import socket
import os
import threading

# Dirección IP y puerto en los que el servidor escucha las conexiones
HOST = '127.0.0.1'
PORT = 3312

# Carpeta en la que se guardarán los archivos recibidos
CARPETA_DESTINO = 'C:/Users/jalex/Documents/ESCOM IPN/ESCOM 7TH SEM/REDES II/P1-SERVERDRIVE/SERVER'


def recibir_archivo(conn):
    # Recibimos el nombre del archivo
    nombre_archivo = conn.recv(1024).decode()
    print('Nombre del archivo:', nombre_archivo)

    # Enviamos una confirmación al cliente
    conn.send(b'OK')

    # Recibimos el tamaño del archivo
    tam = int(conn.recv(1024).decode())
    print('Tamaño del archivo:', tam)

    # Enviamos una confirmación al cliente
    conn.send(b'OK')

    # Ruta completa del archivo en la carpeta destino
    ruta_archivo = os.path.join(CARPETA_DESTINO, nombre_archivo)

    # Abrimos el archivo en modo escritura binaria
    with open(ruta_archivo, 'wb') as file:
        # Recibimos los datos del archivo en bloques de 1024 bytes
        while tam > 0:
            data = conn.recv(1024)
            file.write(data)
            tam -= len(data)

    print('Archivo recibido y guardado en:', ruta_archivo)

def manejar_conexion(conn, addr):
    print('Conexión establecida con:', addr)

    # Llamamos a la función para recibir el archivo
    recibir_archivo(conn)

    # Cerramos la conexión
    conn.close()

def iniciar_servidor():
    # Creamos el socket y lo vinculamos a la dirección y puerto
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    print('Servidor iniciado. Esperando conexiones...')

    while True:
        # Aceptamos la conexión entrante
        conn, addr = s.accept()

        # Creamos un hilo para manejar la conexión y recibir el archivo
        thread = threading.Thread(target=manejar_conexion, args=(conn, addr))
        thread.start()

        # Imprimimos el número de hilos activos
        print('Hilos activos:', threading.active_count() - 1)


# Llamamos a la función para iniciar el servidor
iniciar_servidor()
