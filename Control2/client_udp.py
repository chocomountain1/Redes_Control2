import socket
#Dirección del servidor utilizando credenciales de la MV
SERVER_ADRESS = ("10.0.2.15",8000)

#Creamos el socket no orientado a conexión basado en UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Pedimos al usuario que ingrese la ruta absoluta del archivo, en este caso, el archivo está en la misma carpeta que client.udp.py
path = input("Ingrese la ruta del archivo: ")

#Se utiliza rb pues así nos queda de inmediato en bytes la información por chunk de data
with open(path, "rb") as f:
    while True:
        #Limitamos la lectura a 16bytes
        chunk = f.read(16)

        if not chunk:
           break

        sock.sendto(chunk, SERVER_ADRESS)

#Agregamos un print sólo para saber si el archivo se envió
print("Archivo enviado")