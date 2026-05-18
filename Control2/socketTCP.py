import socket
import random

class SocketTCP:
    def __init__(self):
        # inicializamos las variables que definen un SocketTCP
        # los datos que aun no sabemos se ponen como None

        #En cada instancia de esta clase tendremos acceso a un socket udp interno
        self.socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.direccion_destino = ("10.0.2.15", 8000) 
        self.direccion_origen = ("10.0.2.15", 8000) #Ambas las dejamos iguales por ahora, pero podrían sobreescribirse
        self.numero_secuencia_cliente = random.randint(0, 100)
        self.numero_secuencia_servidor = random.randint(0, 100)
        self.msg = None
        self.timeout = 0
        self.length = 0

    def set_socket_udp(self, socket_udp):
        self.socket_udp = socket_udp

    def set_direccion_destino(self, direccion_destino):
        self.direccion_destino = direccion_destino

    def get_direccion_destino(self):
        return self.direccion_destino

    def set_direccion_origen(self, direccion_origen):
        self.direccion_origen = direccion_origen

    def get_direccion_origen(self):
        return self.direccion_origen

    def set_numero_secuencia_cliente(self, numero_secuencia):
        self.numero_secuencia_cliente = numero_secuencia

    def set_numero_secuencia_servidor(self, numero_secuencia):
        self.numero_secuencia_servidor = numero_secuencia
    
    def set_msg(self, msg):
        self.msg = msg

    def set_timeout(self, timeout):
        self.timeout = timeout
    
    def set_length(self, length):
        self.length = length

    # Método estático que tomando un segmento TCP de la forma
    # [SYN]|||[ACK]|||[FIN]|||[SEQ]|||[DATOS] lo pasa a un diccionario
    #Agregamos que sea un método estático para que no se pase self como argumento
    @staticmethod
    def parse_segment(TCP_segment):

        #Decodeamos dentro puesto que asumimos que TCP_segment viene en bytes
        decoded_seg = TCP_segment.decode()

        #Separamos por |||
        var_list = decoded_seg.split("|||")
        
        return {
            "syn": var_list[0],
            "ack": var_list[1],
            "fin": var_list[2],
            "seq": var_list[3],
            "data": var_list[4]
        }
    
    # Método estático que dado seq y una fuente de data crea un segmento TCP de la forma
    # [SYN]|||[ACK]|||[FIN]|||[SEQ]|||[DATOS] retornando dicho string
    #Agregamos que sea un método estático para que no se pase self como argumento
    @staticmethod
    def create_segment(syn, ack, fin, seq, data):
        
        return f"{syn}|||{ack}|||{fin}|||{seq}|||{data}"

    
    def bind(self, address): 
        self.socket_udp.bind(address)
        self.set_direccion_origen(address)

    def connect(self,address):
        self.set_direccion_destino(address)

        # Envía el syn para establecer conexión, primera parte del handshake
        segment1 = self.create_segment(1, 0, 0, self.numero_secuencia_cliente, "")
        self.socket_udp.sendto(segment1.encode(), address)

        # Se recibe respuesta del server y preparamos la respuesta para enviar tercera parte del handshake
        response, server_address = self.socket_udp.recvfrom(1024)
        response2 = self.parse_segment(response)

        if int(response2["syn"]) == 1 and int(response2["ack"]) == 1:
            #Se crea el 3 segmento de los pasos del handshake
            segment3 = self.create_segment(0, 1, 0, self.numero_secuencia_cliente+1, "")
            self.socket_udp.sendto(segment3.encode(), server_address)
            self.set_direccion_destino((server_address[0], server_address[1]+1))
            self.set_numero_secuencia_cliente(self.numero_secuencia_cliente+1)
        else:
            print("El servidor no devolvió un mensaje syn ack")

    def accept(self):
        new_adress = (self.direccion_destino[0],self.direccion_destino[1]+1)
        response, client_adress = self.socket_udp.recvfrom(1024)

        response = self.parse_segment(response)
        if int(response['syn']) == 1:
            #Creamos el segmento 2 de los pasos del handshake
            segment2 = self.create_segment(1,1,0,self.numero_secuencia_servidor+1,"")
            self.socket_udp.sendto(segment2.encode(), client_adress)
            self.set_direccion_destino(client_adress)
            self.set_numero_secuencia_servidor(self.numero_secuencia_servidor+1)
            response, _ = self.socket_udp.recvfrom(1024)
            response = self.parse_segment(response)
            numero_secuencia_cliente = response["seq"]

            if int(response["ack"]) == 1:
                return_tcp = SocketTCP()
                return_tcp.set_direccion_origen(new_adress)
                return_tcp.set_direccion_destino(client_adress)
                return_tcp.set_numero_secuencia_servidor(self.numero_secuencia_servidor)
                return_tcp.set_numero_secuencia_cliente(numero_secuencia_cliente)
                return_tcp.bind(new_adress)
                print("3-Way-Handshake concretado")
                return (return_tcp, new_adress)
            else:
                print("El cliente no devolvió un mensaje ack")
        else:
            print("El cliente no devolvió un mensaje syn")
