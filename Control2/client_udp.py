import socketTCP

#Dirección del servidor utilizando credenciales de la MV
SERVER_ADRESS = ("10.0.2.15",8000)

#Creamos el socket no orientado a conexión basado en UDP
tcp_sock = socketTCP.SocketTCP()
#Pedimos al usuario que ingrese la ruta absoluta del archivo, en este caso, el archivo está en la misma carpeta que client.udp.py
path = input("Ingrese la ruta del archivo: ")

tcp_sock.connect(SERVER_ADRESS)
#Se utiliza rb pues así nos queda de inmediato en bytes la información por chunk de data
seq = 0
with open(path, "rb") as f:
    while True:
        #Limitamos la lectura de los datos a 16bytes
        chunk = f.read(16)

        #Si no hay más que leer entonces salimos
        if not chunk:
           break
        
        #Antes de wrappear la data dentro del segmento la decodeamos para que bytes -> str
        data = chunk.decode()
        
        #Aquí usamos el método estático del socket TCP para crear un segmento TCP
        segment = tcp_sock.create_segment(1,0,0,seq,data).encode()
        
        #Aumentamos seq a lo que alcanzamos a leer
        seq += len(chunk)
        
        #Finalmente mandamos el segmento al servidor
        tcp_sock.socket_udp.sendto(segment, tcp_sock.direccion_destino)

#Agregamos un print sólo para saber si el archivo se envió
print("Archivo enviado")