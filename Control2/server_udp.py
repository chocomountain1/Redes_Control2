import socketTCP

#Creamos socket no orientado a conexión basado en UDP
tcp_sock = socketTCP.SocketTCP()

#Lo asociamos a las credenciales de la MV
tcp_sock.socket_udp.bind(("10.0.2.15", 8000))

while True:
    #Aseguramos de leer todo el segmento entrante
    segment,adrr = tcp_sock.socket_udp.recvfrom(1024)
    
    #Usamos el método estático del socket TCP para tener acceso al diccionario de atributos relevantes de un segmento TCP
    dic = tcp_sock.parse_segment(segment)
    
    #Printeamos por cada loop del while, sin preoucuparnos cuando termina
    print(dic["data"])