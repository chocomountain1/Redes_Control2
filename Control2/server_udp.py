import socketTCP

#Creamos socket no orientado a conexión basado en UDP
server_socketTCP = socketTCP.SocketTCP()

#Lo asociamos a las credenciales de la MV
server_socketTCP.bind(("10.0.2.15", 8000))

connection_socketTCP, new_address = server_socketTCP.accept()
while True:
    #Aseguramos de leer todo el segmento entrante
    segment,adrr = connection_socketTCP.socket_udp.recvfrom(1024)
    
    #Usamos el método estático del socket TCP para tener acceso al diccionario de atributos relevantes de un segmento TCP
    dic = connection_socketTCP.parse_segment(segment)
    
    #Printeamos por cada loop del while, sin preoucuparnos cuando termina
    print(dic["data"])