import socket

#Creamos socket no orientado a conexión basado en UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Lo asociamos a las credenciales de la MV
sock.bind(("10.0.2.15", 8000))

while True:
    data,adrr = sock.recvfrom(16)

    #Printeamos por cada loop del while, sin preoucuparnos cuando termina
    print(data)