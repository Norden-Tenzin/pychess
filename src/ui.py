#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys
from helper_functions import *
from pygame.locals import *
from constants import *
# from main import *

# Setup pygame/window ---------------------------------------- #

pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((SIZE, SIZE))
mainClock = pygame.time.Clock()

font_name = "segoeulblack"
title = pygame.font.SysFont(font_name, 80, 1)
text = pygame.font.SysFont(font_name, 40, 1)

fonts = pygame.font.get_fonts()
click = False

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

def main_menu():
    i = 0
    click = False
    while True:
        screen.fill(LIGHTDARK)
        mx, my = pygame.mouse.get_pos()
        draw_text('Chess', title, WHITE, screen, 10, 10)
        
        # offline
        draw_button('Offline', text, WHITE, screen, 10, 10, 25, 100, SIZE-50, 50, DARKER, offline, mx, my, click)
        # host game
        draw_button('Host', text, WHITE, screen, 10, 10, 25, 160, SIZE-50, 50, DARKER, host, mx, my, click)
        # join game
        draw_button('Join', text, WHITE, screen, 10, 10, 25, 220, SIZE-50, 50, DARKER, join, mx, my, click)
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
    pass

def host():
    pass

def join():
    pass

def options():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('options', title, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

if __name__ == "__main__": 
    main_menu()