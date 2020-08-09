# this will hold the classes of the chess pieces

import pygame
import random
from constants import *


class Key(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, id):
        super(Key, self).__init__()
        self.image = pygame.image.load(W_KING)
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos


pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("This is a new Window")

done = False
# clock = pygame.time.Clock()
key_list = pygame.sprite.Group()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x = pos[0]-25
            y = pos[1]-25
            if event.button == 3:
                key_list.add(Key(x, y, len(key_list)+1))
            elif event.button == 1:
                for key in key_list:
                    if key.rect.collidepoint(pos):
                        key.clicked = True
        if event.type == pygame.MOUSEBUTTONUP:
            for key in key_list:
                key.clicked = False
            drag_id = 0
    for key in key_list:
        if key.clicked == True:
            pos = pygame.mouse.get_pos()
            key.rect.x = pos[0] - (int(key.rect.width/2))
            key.rect.y = pos[1] - (int(key.rect.height/2))
    screen.fill(BLACK)
    key_list.draw(screen)
    pygame.display.flip()
    # clock.tick(60)
pygame.quit()
