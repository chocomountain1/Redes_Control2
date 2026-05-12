import socket

class SocketTCP:
    def __init__(self):
        # inicializamos las variables que definen un SocketTCP
        # los datos que aun no sabemos se ponen como None

        #En cada instancia de esta clase tendremos acceso a un socket udp interno
        self.socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.direccion_destino = ("10.0.2.15", 8000) 
        self.direccion_origen = ("10.0.2.15", 8000) #Ambas las dejamos iguales por ahora, pero podrían sobreescribirse
        self.numero_secuencia = 0
        self.msg = None
        self.timeout = 0
        self.length = 0

    def set_socket_udp(self, socket_udp):
        self.socket_udp = socket_udp

    def set_direccion_destino(self, direccion_destino):
        self.direccion_destino = direccion_destino

    def set_direccion_origen(self, direccion_origen):
        self.direccion_origen = direccion_origen

    def set_numero_secuencia(self, numero_secuencia):
        self.numero_secuencia = numero_secuencia
    
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
        var_list = TCP_segment.split("|||")
        print(var_list)
        #1ra iteracion: "0|||0|||0|||0|||''"
        #2da iteracion: "0|||0|||0|||0||''"
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

    
