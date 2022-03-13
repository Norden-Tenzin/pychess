#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys
from helper_functions import *
from main import *

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((SIZE, SIZE))

font = pygame.font.SysFont(None, 20)
# print(str(pygame.font.get_fonts()) + "\n")

fonts = pygame.font.get_fonts()
click = False

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main_menu():
    i = 0
    while True:
        screen.fill((0,0,0))

        draw_text('Chess', pygame.font.SysFont(fonts[i], 40), (255, 255, 255), screen, 20, 20)
        draw_text(fonts[i], pygame.font.SysFont(None, 20), (255, 255, 255), screen, 20, 70)

        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(100, 100, 200, 50)
        button_2 = pygame.Rect(100, 175, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        draw_text('Game', pygame.font.SysFont(fonts[i], 40), (255, 255, 255), screen, 150, 100)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        draw_text('Option', pygame.font.SysFont(fonts[i], 40), (255, 255, 255), screen, 150, 170)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_RIGHT:
                    if(i < len(fonts)+1):
                        i += 1
                    else:
                        i = 0
                if event.key == K_LEFT:
                    if(i < len(fonts)+1):
                        i -= 1
                    else:
                        i = 0
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 
def game():
    running = True
    while running:
        main()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
 
def options():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('options', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

main_menu()