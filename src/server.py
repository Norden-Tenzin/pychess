# Python program to implement server side of chat room.
import socket
import select
import sys
import json
'''Replace "thread" with "_thread" for python 3'''
from _thread import *
from uuid import uuid4
 
def server():
    """The first argument AF_INET is the address domain of the
    socket. This is used when we have an Internet Domain with
    any two hosts The second argument is the type of socket.
    SOCK_STREAM means that data or characters are read in
    a continuous flow."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    IP_address = "127.0.0.1"
    Port = 6000
    
    """
    binds the server to an entered IP address and at the
    specified port number.
    The client must be aware of these parameters
    """
    server.bind((IP_address, Port))
    
    """
    listens for 100 active connections. This number can be
    increased as per convenience.
    """
    server.listen(2)
    
    list_of_clients = []
    
    def clientthread(conn, addr):        
        while True:
            try:
                message = json.loads(conn.recv(2048).decode('utf-8'))
                # print(message)
                if message:
                    # register client uid
                    if message["code"] == 100:
                        print("CODE: 100")
                        # [{"conn": conn, "uid": "", "color": 0}]
                        i = list_of_clients.index(next(filter(lambda n: n.get('conn') == conn, list_of_clients)))
                        list_of_clients[i]["uid"] = message["uid"]

                        print("PLAYER JOINED: {}".format(list_of_clients[i]["uid"]))
                        # print(list_of_clients)

                    if message["code"] == 110:
                        print("CODE: 110")
                        player_data = message["player"]
                        i = list_of_clients.index(next(filter(lambda n: n.get('uid') == player_data["uid"], list_of_clients)))
                        list_of_clients[i]["color"] = player_data["color"]

                        data = {"code": 210, "players": [{"user": i["user"], "color": i["color"]} for i in list_of_clients]}
                        message_to_send = json.dumps(data).encode('utf-8')
                        print("SERVER")
                        print(message_to_send)
                        # send to one
                        broadcast_to_one(message_to_send, conn)

                    # """prints the message and address of the
                    # user who just sent the message on the server
                    # terminal"""
                    # message_to_send = "<{}> {}".format(uid, message)
                    # print(message_to_send)
                    # # Calls broadcast function to send message to all
                    # broadcast(message_to_send.encode("utf-8") , conn)

                else:
                    """message may have no content if the connection
                    is broken, in this case we remove the connection"""
                    print("CONNECTION CLOSED: {}".format(conn))
                    remove(conn)
            except:
                continue

    def broadcast_to_one(message, connection):
        for client in list_of_clients:
            if client == connection:
                try:
                    client.send(message)
                except:
                    client.close()
                    # if the link is broken, we remove the client
                    remove(client)

    def broadcast_to_all(message):
        for client in list_of_clients:
            try:
                client.send(message)
            except:
                client.close()
                # if the link is broken, we remove the client
                remove(client)
    
    """Using the below function, we broadcast the message to all
    clients who's object is not the same as the one sending
    the message """
    def broadcast(message, connection):
        for client in list_of_clients:
            if client != connection:
                try:
                    client.send(message)
                except:
                    client.close()
                    # if the link is broken, we remove the client
                    remove(client)
    
    """The following function simply removes the object
    from the list that was created at the beginning of
    the program"""
    def remove(connection):
        if connection in list_of_clients:
            list_of_clients.remove(connection)
    
    while True:
        """Accepts a connection request and stores two parameters,
        conn which is a socket object for that user, and addr
        which contains the IP address of the client that just
        connected"""
        conn, addr = server.accept()
    
        """Maintains a list of clients for ease of broadcasting
        a message to all available people in the chatroom"""
        if len(list_of_clients) < 2:
            list_of_clients.append({"conn": conn, "uid": "", "color": 0})
            # prints the address of the user that just connected
            print(addr[0] + " connected")
            start_new_thread(clientthread,(conn,addr))    
        else:
            print(addr[0] + " not connected")
            print("Chat is full")
            conn.send("Chat is full".encode('utf-8'))
        # creates and individual thread for every user
        # that connects
        
    conn.close()
    server.close()

if __name__ == "__main__":
    server()