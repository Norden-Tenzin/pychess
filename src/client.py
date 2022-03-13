import sys
from twisted.internet import reactor
from twisted.internet.protocol import Protocol
from twisted.internet.protocol import ClientFactory 
from twisted.internet.endpoints import TCP4ClientEndpoint

class Client(Protocol):
    def __init__(self):
        reactor.callInThread(self.send_Data)    
        self.transport.write(sys.argv[0].encode("utf-8"))

    def dataReceived(self, data):
        data = data.decode("utf-8")
        print(data)

    def send_Data(self):
        while True:
            self.transport.write(input().encode("utf-8"))

class ClientFactory(ClientFactory):
    def buildProtocol(self, addr):
        return Client()

if __name__ == "__main__":
    endpoint = TCP4ClientEndpoint(reactor, "localhost", 8000)
    endpoint.connect(ClientFactory())
    reactor.run()