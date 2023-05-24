from __future__ import print_function

import sys
import uuid
from time import sleep
from sys import stdin, exit
from PodSixNet.Connection import connection, ConnectionListener
from ui_helper import *

# This example uses Python threads to manage async input from sys.stdin.
# This is so that I can receive input from the console whilst running the server.
# Don't ever do this - it's slow and ugly. (I'm doing it for simplicity's sake)
from _thread import *

def lobby(screen, players):
    connection.Send({"action": "message", "message": "INLOBBY"})
    # player_data = {"uid": uid, "color": 0}
    # sample message
    # {"status": "lobby", "data": [
    #     {"user": "<>", "color": 0},
    # ]}
    def draw_lobby_player(screen, player, font, color, surface, list_x, list_y, list_w, list_h, list_color, mx, my, click):
        outter_rect = pygame.Rect(list_x, list_y, list_w, list_h)
        white_button_rect = pygame.Rect(list_x + list_w - 70, list_y + math.floor((50 - 25)/ 2), 25, 25)
        black_button_rect = pygame.Rect(list_x + list_w - 35, list_y + math.floor((50 - 25)/ 2), 25, 25)
        if white_button_rect.collidepoint((mx, my)):
            if click:
                player['color'] = 0
        if black_button_rect.collidepoint((mx, my)):
            if click:
                player['color'] = 1
        pygame.draw.rect(screen, list_color, outter_rect)
        pygame.draw.rect(screen, WHITE, white_button_rect)
        pygame.draw.rect(screen, BLACK, black_button_rect)

        def draw_tick(color):
            if color == 0:
                screen.blit(tick_image, (list_x + list_w - 70, list_y + math.floor((50 - 25)/ 2)))
            elif color == 1:
                screen.blit(tick_image, (list_x + list_w - 35, list_y + math.floor((50 - 25)/ 2)))

        draw_tick(player['color'])
        draw_text(player['user'], font, color, surface, list_x +  5, list_y + 5)

    def draw_lobby_players(lst_player, font, color, surface, list_x, list_y, list_w, list_h, list_color, mx, my, click):
        for i, player in enumerate(lst_player):
            draw_lobby_player(player, font, color, surface, list_x, list_y + (list_h + 5)*i, list_w, list_h, list_color, mx, my, click)

    # def refresh():
    #     print("HERE1")
    #     # send my settings
    #     data = {"code": 110, "player": player_data}
    #     message_to_send = json.dumps(data).encode('utf-8')
    #     server.send(message_to_send)

    #     print("HERE2")

    #     data = server.recv(2048)
    #     message = json.dumps(data).encode('utf-8')
    #     print(message)
        
    # refresh(server)

    # data = {"code": 110, "player": player_data}
    # message = json.dumps(data).encode('utf-8')
    # server.send(message)

    has_started = False
    click = False
    # data = {"status": "lobby", "data": [
    #     {"user": "<uid1>", "color": 0}, {"user": "<uid2>", "color": 1}
    # ]}
    lst_player = players
    def blank():
        pass

    while not has_started:
        screen.fill(DARK)
        mx, my = pygame.mouse.get_pos()
        draw_text('Lobby', title, WHITE, screen, 25, 35)
        draw_button('< back', back, WHITE, screen, 5, 5, 25, 10, 60, 20, DARKER, blank, mx, my, click)
        draw_button('⟳ refresh', back, WHITE, screen, 5, 5, 300, 10, 60, 20, DARKER, blank, mx, my, click)
        draw_lobby_players(lst_player, back, WHITE, screen, 25, 100, SIZE-50, 50, DARKER, mx, my, click)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False
        pygame.display.update()
        mainClock.tick(60)

# TODO remove hardcoded values
# def connect_to_server():
#     server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     IP_address = "127.0.0.1"
#     Port = 6000
#     server.connect((IP_address, Port))
#     data = {"code": 100, "uid": uid}
#     message = json.dumps(data)
#     server.send(message.encode('utf-8'))
#     return server

class Client(ConnectionListener):
    def __init__(self, host, port, screen):
        self.screen = screen
        self.players = []
        self.Connect((host, port))
        print("Chat client started")
        print("Ctrl-C to exit")
        connection.Send({"action": "id", "id": str(uuid.uuid4())})
        t = start_new_thread(self.InputLoop, ())
    
    def Loop(self):
        connection.Pump()
        self.Pump()
    
    def InputLoop(self):
        lobby(self.screen, self.players)
        # horrid threaded input loop
        # continually reads from stdin and sends whatever is typed to the server
        # while 1:
        #     connection.Send({"action": "message", "message": stdin.readline().rstrip("\n")})
    
    #######################################
    ### Network event/message callbacks ###
    ####################################### 
    
    def Network_players(self, data):
        self.players = data['players']
        print("*** players: " + ", ".join([p for p in data['players']]))
    
    def Network_message(self, data):
        print(data['who'] + ": " + data['message'])
    
    # built in stuff

    def Network_connected(self, data):
        print("You are now connected to the server")
    
    def Network_error(self, data):
        print('error:', data['error'][1])
        connection.Close()
    
    def Network_disconnected(self, data):
        print('Server disconnected')
        exit()

if __name__ == '__main__':
    host, port = "127.0.0.1", "8088"
    c = Client(host, int(port))
    while 1:
        c.Loop()
        sleep(0.001)
        
