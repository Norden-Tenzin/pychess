from helperfunctions import *

# this will hold the classes of the chess pieces


class Chessmen(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


# king queen bishop knight rook pawn
class King(Chessmen):
    def __init__(self, name, xpos, ypos):
        super().__init__()
        self.clicked = False
        self.name = name
        if(self.name.islower()):
            self.image = pygame.image.load(W_KING)
        else:
            self.image = pygame.image.load(B_KING)
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

    def moveset(self, posx, posy):
        # x = j y = i
        maparr = readGame()
        for i, line in enumerate(maparr):
            for j, tile in enumerate(line):
                if tile.split("-")[1] == self.name:
                    # print("I: " + str(i*50) + " J: " + str(j*50))
                    # print(math.floor(posx/50) * 50)
                    if j*50-(1*50) <= math.floor(posx/50) * 50 <= j*50+(1*50) and i*50-(1*50) <= math.floor(posy/50) * 50 <= i*50+(1*50):
                        return True
                    else:
                        return False

    def possiblemoves(self, posx, posy):
        maparr = readGame()
        if maparr[math.floor(posy/50)][math.floor(posx/50)].find("##") >= 0 and self.moveset(posx, posy):
            return True
        else:
            return False

    def enemydetect(self, posx, posy):  # if the enemy is on that pos
        maparr = readGame()
        if self.name.strip()[0].islower():
            if maparr[math.floor(posy/50)][math.floor(posx/50)].split("-")[1].strip()[0].isupper() and self.moveset(posx, posy):
                return True
            else:
                return False
        elif self.name.strip()[0].isupper():
            if maparr[math.floor(posy/50)][math.floor(posx/50)].split("-")[1].strip()[0].islower() and self.moveset(posx, posy):
                return True
            else:
                return False

    def move(self, posx, posy):
        maparr = readGame()
        # print(np.matrix(maparr))
        if self.possiblemoves(posx, posy):
            writeGame(self, posx, posy)
            self.rect.x = math.floor(posx/50) * 50
            self.rect.y = math.floor(posy/50) * 50
            return 0
        elif self.enemydetect(posx, posy):
            writeGame(self, posx, posy)
            self.rect.x = math.floor(posx/50) * 50
            self.rect.y = math.floor(posy/50) * 50
            return 1
        else:
            for i, line in enumerate(maparr):
                for j, tile in enumerate(line):
                    if tile.split("-")[1] == self.name:
                        # print("I: " + str(i) + " J: " + str(j))
                        self.rect.x = j*50
                        self.rect.y = i*50
            return -1


class Queen(Chessmen):
    def __init__(self, name, xpos, ypos):
        super().__init__()
        self.name = name
        if(self.name.islower()):
            self.image = pygame.image.load(W_QUEEN)
        else:
            self.image = pygame.image.load(B_QUEEN)
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos


class Bishop(Chessmen):
    def __init__(self, name, xpos, ypos):
        super().__init__()
        self.name = name
        if(self.name.islower()):
            self.image = pygame.image.load(W_BISHOP)
        else:
            self.image = pygame.image.load(B_BISHOP)
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos


class Knight(Chessmen):
    def __init__(self, name, xpos, ypos):
        super().__init__()
        self.name = name
        if(self.name.islower()):
            self.image = pygame.image.load(W_KNIGHT)
        else:
            self.image = pygame.image.load(B_KNIGHT)
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos


class Rook(Chessmen):
    def __init__(self, name, xpos, ypos):
        super().__init__()
        self.name = name
        if(self.name.islower()):
            self.image = pygame.image.load(W_ROOK)
        else:
            self.image = pygame.image.load(B_ROOK)
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos


class Pawn(Chessmen):
    def __init__(self, name, xpos, ypos):
        super().__init__()
        self.name = name
        if(self.name.islower()):
            self.image = pygame.image.load(W_PAWN)
        else:
            self.image = pygame.image.load(B_PAWN)
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

    def moveset(self, posx, posy):
        # x = j y = i
        maparr = readGame()
        for i, line in enumerate(maparr):
            for j, tile in enumerate(line):
                if tile.split("-")[1] == self.name:
                    # print("I: " + str(i*50) + " J: " + str(j*50))
                    # print(math.floor(posx/50) * 50)
                    if j*50-(1*50) <= math.floor(posx/50) * 50 <= j*50+(1*50) and i*50-(1*50) <= math.floor(posy/50) * 50 <= i*50+(1*50):
                        return True
                    else:
                        return False

    def possiblemoves(self, posx, posy):
        maparr = readGame()
        if maparr[math.floor(posy/50)][math.floor(posx/50)].find("##") >= 0 and self.moveset(posx, posy):
            return True
        else:
            return False

    def enemydetect(self, posx, posy):  # if the enemy is on that pos
        maparr = readGame()
        if self.name.strip()[0].islower():
            if maparr[math.floor(posy/50)][math.floor(posx/50)].split("-")[1].strip()[0].isupper() and self.moveset(posx, posy):
                return True
            else:
                return False
        elif self.name.strip()[0].isupper():
            if maparr[math.floor(posy/50)][math.floor(posx/50)].split("-")[1].strip()[0].islower() and self.moveset(posx, posy):
                return True
            else:
                return False

    def move(self, posx, posy):
        maparr = readGame()
        # print(np.matrix(maparr))
        if self.possiblemoves(posx, posy):
            writeGame(self, posx, posy)
            self.rect.x = math.floor(posx/50) * 50
            self.rect.y = math.floor(posy/50) * 50
            return 0
        elif self.enemydetect(posx, posy):
            writeGame(self, posx, posy)
            self.rect.x = math.floor(posx/50) * 50
            self.rect.y = math.floor(posy/50) * 50
            return 1
        else:
            for i, line in enumerate(maparr):
                for j, tile in enumerate(line):
                    if tile.split("-")[1] == self.name:
                        # print("I: " + str(i) + " J: " + str(j))
                        self.rect.x = j*50
                        self.rect.y = i*50
            return -1

