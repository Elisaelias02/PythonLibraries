from twisted.internet import reactor, protocol

class MiProtocolo(protocol.Protocol):
    def connectionMade(self):
        print("Cliente conectado")

    def dataReceived(self, data):
        print("Datos recibidos del cliente:", data.decode())
        self.transport.write(b"¡Hola desde el servidor!")

    def connectionLost(self, reason):
        print("Cliente desconectado")

class MiFactoria(protocol.Factory):
    def buildProtocol(self, addr):
        return MiProtocolo()

# Configuración del servidor
puerto = 8000

# Iniciar el servidor
reactor.listenTCP(puerto, MiFactoria())
print("Servidor escuchando en el puerto", puerto)
reactor.run()
