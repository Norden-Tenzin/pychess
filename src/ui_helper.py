import pygame
from helper_functions import *
from pygame.locals import *
from constants import *

font_name = "segoeulblack"
title = pygame.font.SysFont(font_name, 80, 1)
text = pygame.font.SysFont(font_name, 40, 1)
base_font = pygame.font.Font(None, 32)
back = pygame.font.SysFont(font_name, 15, 1)
tick_image = pygame.image.load(TICK)
fonts = pygame.font.get_fonts()
mainClock = pygame.time.Clock()

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def draw_button(screen, text, font, color, surface, fontxoffset, fontyoffset, buttonx, buttony, buttonw, buttonh, buttoncolor, buttonfunc, mx, my, click):
    button_rect = pygame.Rect(buttonx, buttony, buttonw, buttonh)
    if button_rect.collidepoint((mx, my)):
        if click:
            buttonfunc()
    pygame.draw.rect(screen, buttoncolor, button_rect)
    draw_text(text, font, color, surface, buttonx + fontxoffset, buttony + fontyoffset)

def draw_button_main(screen, text, font, color, surface, fontxoffset, fontyoffset, buttonx, buttony, buttonw, buttonh, buttoncolor, buttonfunc, mx, my, click, play_as = 0):
    button_rect = pygame.Rect(buttonx, buttony, buttonw, buttonh)
    if button_rect.collidepoint((mx, my)):
        if click:
            buttonfunc(play_as)
    pygame.draw.rect(screen, buttoncolor, button_rect)
    draw_text(text, font, color, surface, buttonx + fontxoffset, buttony + fontyoffset)
