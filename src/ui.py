#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys
from helper_functions import *
from pygame.locals import *
from constants import *
from main import main
from uuid import uuid4
import json

# server
from _thread import *
from server import server
import socket
import select
import sys
# from main import *

# Setup pygame/window ---------------------------------------- #

pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode(SCREEN_SIZE)
mainClock = pygame.time.Clock()

font_name = "segoeulblack"
title = pygame.font.SysFont(font_name, 80, 1)
text = pygame.font.SysFont(font_name, 40, 1)
base_font = pygame.font.Font(None, 32)
back = pygame.font.SysFont(font_name, 15, 1)
tick_image = pygame.image.load(TICK)
fonts = pygame.font.get_fonts()

click = False

# global
uid = ""

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def draw_button(text, font, color, surface, fontxoffset, fontyoffset, buttonx, buttony, buttonw, buttonh, buttoncolor, buttonfunc, mx, my, click):
    button_rect = pygame.Rect(buttonx, buttony, buttonw, buttonh)
    if button_rect.collidepoint((mx, my)):
        if click:
            buttonfunc()
    pygame.draw.rect(screen, buttoncolor, button_rect)
    draw_text(text, font, color, surface, buttonx + fontxoffset, buttony + fontyoffset)

def draw_button_main(text, font, color, surface, fontxoffset, fontyoffset, buttonx, buttony, buttonw, buttonh, buttoncolor, buttonfunc, mx, my, click, play_as = 0):
    button_rect = pygame.Rect(buttonx, buttony, buttonw, buttonh)
    if button_rect.collidepoint((mx, my)):
        if click:
            buttonfunc(play_as)
    pygame.draw.rect(screen, buttoncolor, button_rect)
    draw_text(text, font, color, surface, buttonx + fontxoffset, buttony + fontyoffset)

def main_menu():
    print("INMAIN")
    global uid
    # set uuid 
    if uid == "":
        uid = str(uuid4())

    i = 0
    click = False
    while True:
        screen.fill(DARK)
        mx, my = pygame.mouse.get_pos()
        draw_text('Chess', title, WHITE, screen, 25, 35)
        
        # offline   
        draw_button('Offline', text, WHITE, screen, 10, 10, 25, 100, SIZE-50, 50, DARKER, offline, mx, my, click)
        # host game
        draw_button('Host Game', text, WHITE, screen, 10, 10, 25, 160, SIZE-50, 50, DARKER, host, mx, my, click)
        # join game
        draw_button('Join Game', text, WHITE, screen, 10, 10, 25, 220, SIZE-50, 50, DARKER, join, mx, my, click)
        # options
        draw_button('Options', text, WHITE, screen, 10, 10, 25, 280, SIZE-50, 50, DARKER, options, mx, my, click)
        click = False   
        
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
        pygame.display.update()
        mainClock.tick(60)
 
def game():
    running = True
    while running:
        # main()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

def offline():
    running = True
    click = False
    while running:
        screen.fill(DARK)
        mx, my = pygame.mouse.get_pos()
        draw_text('Player', title, WHITE, screen, 25, 35)
        draw_text('Color', title, WHITE, screen, 25, 80)
        
        draw_button('< back', back, WHITE, screen, 5, 5, 25, 10, 60, 20, DARKER, main_menu, mx, my, click)

        draw_button_main('White', text, BLACK, screen, 10, 10, 25, 140, SIZE-50, 50, WHITE, main, mx, my, click, 0)
        draw_button_main('Black', text, WHITE, screen, 10, 10, 25, 200, SIZE-50, 50, BLACK, main, mx, my, click, 1)

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
        pygame.display.update()
        mainClock.tick(60)

def lobby(server):
    print("INLOBBY")
    player_data = {"uid": uid, "color": 0}
    # sample message
    # {"status": "lobby", "data": [
    #     {"user": "<>", "color": 0},
    # ]}

    def draw_lobby_player(player, font, color, surface, list_x, list_y, list_w, list_h, list_color, mx, my, click):
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

    def refresh(server):
        print("HERE1")
        # send my settings
        data = {"code": 110, "player": player_data}
        message_to_send = json.dumps(data).encode('utf-8')
        server.send(message_to_send)

        print("HERE2")

        data = server.recv(2048)
        message = json.dumps(data).encode('utf-8')
        print(message)
        
    refresh(server)

    # data = {"code": 110, "player": player_data}
    # message = json.dumps(data).encode('utf-8')
    # server.send(message)

    has_started = False
    click = False
    data = {"status": "lobby", "data": [
        {"user": "<uid1>", "color": 0}, {"user": "<uid2>", "color": 1}
    ]}
    lst_player = data['data']
    
    while not has_started:
        screen.fill(DARK)
        mx, my = pygame.mouse.get_pos()
        draw_text('Lobby', title, WHITE, screen, 25, 35)
        draw_button('< back', back, WHITE, screen, 5, 5, 25, 10, 60, 20, DARKER, main_menu, mx, my, click)
        draw_button('⟳ refresh', back, WHITE, screen, 5, 5, 300, 10, 60, 20, DARKER, main_menu, mx, my, click)
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
def connect_to_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IP_address = "127.0.0.1"
    Port = 6000
    server.connect((IP_address, Port))
    data = {"code": 100, "uid": uid}
    message = json.dumps(data)
    server.send(message.encode('utf-8'))
    return server

def host():
    # start server
    start_new_thread(server,())  
    # threading.Thread(target=server).start()
    # join server
    server_var = connect_to_server()
    lobby(server_var)
    # call lobby
    pass

def join():
    # join server
    server_var = connect_to_server()
    lobby(server_var)
    # call lobby
    pass 

    # TODO server selection screen

    # active = False
    # input_rect = pygame.Rect(200, 200, 140, 32)
    # user_text = ''
    # while True:
    #     for event in pygame.event.get():
    
    #     # if user types QUIT then the screen will close
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             sys.exit()
    
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             if input_rect.collidepoint(event.pos):
    #                 active = True
    #             else:
    #                 active = False
    
    #         if event.type == pygame.KEYDOWN:
    
    #             # Check for backspace
    #             if event.key == pygame.K_BACKSPACE:
    
    #                 # get text input from 0 to -1 i.e. end.
    #                 user_text = user_text[:-1]
    
    #             # Unicode standard is used for string
    #             # formation
    #             else:
    #                 user_text += event.unicode
        
    #     # it will set background color of screen
    #     screen.fill((255, 255, 255))
    
    #     if active:
    #         color = DARK
    #     else:
    #         color = LIGHTDARK
            
    #     # draw rectangle and argument passed which should
    #     # be on screen
    #     pygame.draw.rect(screen, color, input_rect)
    
    #     text_surface = base_font.render(user_text, True, (255, 255, 255))
        
    #     # render at position stated in arguments
    #     screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
        
    #     # set width of textfield so that text cannot get
    #     # outside of user's text input
    #     input_rect.w = max(100, text_surface.get_width()+10)
        
    #     # display.flip() will update only a portion of the
    #     # screen to updated, not full area
    #     pygame.display.flip()
        
    #     # clock.tick(60) means that for every second at most
    #     # 60 frames should be passed.
    #     mainClock.tick(60)

def options():
    running = True
    click = False
    while running:
        screen.fill(DARK)
        mx, my = pygame.mouse.get_pos()
        draw_text('Option', title, WHITE, screen, 25, 35)
        
        draw_button('< back', back, WHITE, screen, 5, 5, 25, 10, 60, 20, DARKER, main_menu, mx, my, click)

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

if __name__ == "__main__": 
    main_menu()