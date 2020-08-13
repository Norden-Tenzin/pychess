# this will hold the classes of the chess pieces

import pygame
import random
from constants import *

class Chessmen(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.clicked = False
        self.xpos = xpos
        self.ypos = ypos
        

class King(Chessmen):
    def __init__(self,name, xpos, ypos): ## maybe pass in the text for king and figur out which
        super().__init__()
        self.name = name
        if(self.name.islower()):
            self.image = pygame.image.load(W_KING)
        else:
            self.image = pygame.image.load(W_KING)
        self.rect = self.image.get_rect()

        self.rect.x = self.xpos
        self.rect.y = self.ypos
    def show(self):
        print(self.name, self.xpos, self.ypos)
    def possiblemove(self):
        x = 10 #just here to take up space

king = King("ki",0,0)
king.show()
# pygame.init()

# screen = pygame.display.set_mode(SIZE)
# pygame.display.set_caption("This is a new Window")

# done = False
# # clock = pygame.time.Clock()
# key_list = pygame.sprite.Group()

# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True

#         if event.type == pygame.MOUSEBUTTONDOWN:
#             pos = pygame.mouse.get_pos()
#             x = pos[0]
#             y = pos[1]
#             if event.button == 3:
#                 key_list.add(Chessmen(x, y))
#             elif event.button == 1:
#                 for chesspiece in key_list:
#                     if chesspiece.rect.collidepoint(pos):
#                         chesspiece.clicked = True
#         if event.type == pygame.MOUSEBUTTONUP:
#             for chesspiece in key_list:
#                 chesspiece.clicked = False
#             drag_id = 0
#     for chesspiece in key_list:
#         if chesspiece.clicked == True:
#             pos = pygame.mouse.get_pos()
#             chesspiece.rect.x = pos[0] - (int(chesspiece.rect.width/2))
#             chesspiece.rect.y = pos[1] - (int(chesspiece.rect.height/2))
#     screen.fill(BLACK)
#     key_list.draw(screen)
#     pygame.display.flip()
#     # clock.tick(60)
# pygame.quit()
