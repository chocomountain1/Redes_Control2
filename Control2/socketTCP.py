class SocketTCP:
    def __init__(self):
        # inicializamos las variables que definen un SocketTCP
        # los datos que aun no sabemos se ponen como None
        self.socket_udp = None
        self.direccion_destino = None
        self.direccion_origen = None
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

