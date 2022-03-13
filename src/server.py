import names
from twisted.internet import reactor
from twisted.internet.protocol import Protocol
from twisted.internet.protocol import ServerFactory 
from twisted.internet.endpoints import TCP4ServerEndpoint

class User():
    def __init__(self, user):
        self.userSelf = user
        self.userName = names.get_first_name()

class Server(Protocol):
    def __init__(self, users):
        self.users = users

    def connectionMade(self):
        print("New Connection")
        self.users.append(User(self))
        self.transport.write("Hello from Server".encode("utf-8"))

    def dataReceived(self, data):
        stringData = data.decode("utf-8")
        for user in self.users:
            if user.userSelf != self:
                user.userSelf.transport.write((user.userName+"\n"+"    "+stringData).encode("utf-8"))

class ServerFactory(ServerFactory):
    def __init__(self):
        self.users = []

    def buildProtocol(self, addr):
        return Server(self.users)

if __name__ == "__main__":
    endpoint = TCP4ServerEndpoint(reactor, 8000)
    endpoint.listen(ServerFactory())
    reactor.run()