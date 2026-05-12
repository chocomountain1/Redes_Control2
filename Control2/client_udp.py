import socketTCP

#Dirección del servidor utilizando credenciales de la MV
SERVER_ADRESS = ("10.0.2.15",8000)

#Creamos el socket no orientado a conexión basado en UDP
tcp_sock = socketTCP.SocketTCP()

#Pedimos al usuario que ingrese la ruta absoluta del archivo, en este caso, el archivo está en la misma carpeta que client.udp.py
path = input("Ingrese la ruta del archivo: ")

seq = 0
#Se utiliza rb pues así nos queda de inmediato en bytes la información por chunk de data
with open(path, "rb") as f:
    while True:
        #Limitamos la lectura a 16bytes
        chunk = f.read(16)

        if not chunk:
           break
        
        data = chunk.decode()
        segment = tcp_sock.create_segment(0,0,0,seq,data).encode()

        seq += len(chunk)
        tcp_sock.socket_udp.sendto(segment, SERVER_ADRESS)

#Agregamos un print sólo para saber si el archivo se envió
print("Archivo enviado")