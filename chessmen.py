from helperfunctions import *


# this will hold the classes of the chess pieces
class Chessmen(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


# king queen bishop knight rook pawn
class King(Chessmen):
    def __init__(self, name, location, xpos, ypos):
        super().__init__()
        self.clicked = False
        self.name = name
        self.location = location
        if(self.name.islower()):
            self.image = pygame.image.load(W_KING)
        else:
            self.image = pygame.image.load(B_KING)
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

    def moveset(self, posx, posy):
        maparr = readGame()
        for i, line in enumerate(maparr):
            for j, tile in enumerate(line):
                if tile.split("-")[1] == self.name:
                    if j-1 <= math.floor(posx/50) <= j+1 and i-1 <= math.floor(posy/50) <= i+1:
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
                        self.rect.x = j*50
                        self.rect.y = i*50
            return -1

class Queen(Chessmen):
    def __init__(self, name, location, xpos, ypos):
        super().__init__()
        self.name = name
        self.location = location
        if(self.name.islower()):
            self.image = pygame.image.load(W_QUEEN)
        else:
            self.image = pygame.image.load(B_QUEEN)
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

    def moveset(self, posx, posy):
        maparr = readGame()
        pos = locationToPos(self.location)
        xoffset = abs(math.floor(posx/50) - pos[0])
        yoffset = abs(math.floor(posy/50) - pos[1])

        if 0 <= math.floor(posx/50) <= 7 and math.floor(posy/50) == pos[1]:
            return True
        elif math.floor(posx/50) == pos[0] and 0 <= math.floor(posy/50) <= 7:
            return True
        elif xoffset == yoffset:
            return True
        else:
            return False

    def possiblemoves(self, posx, posy):
        maparr = readGame()
        if maparr[math.floor(posy/50)][math.floor(posx/50)].find("##") >= 0 and self.moveset(posx, posy):
            return True
        else:
            return False

    def enemydetect(self, posx, posy):
        maparr = readGame()
        pos = locationToPos(self.location)
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
        location = locationToPos(self.location)
        newlocation = ""

        if self.possiblemoves(posx, posy):
            writeGame(self, posx, posy)
            self.rect.x = math.floor(posx/50) * 50
            self.rect.y = math.floor(posy/50) * 50
            location[0] = math.floor(posx/50)
            location[1] = math.floor(posy/50)
            newlocation = posToLocation(location)
            self.location = newlocation
            return 0
        elif self.enemydetect(posx, posy):
            writeGame(self, posx, posy)
            self.rect.x = math.floor(posx/50) * 50
            self.rect.y = math.floor(posy/50) * 50
            location = [math.floor(posx/50), math.floor(posy/50)]
            newlocation = posToLocation(location)
            self.location = newlocation
            return 1
        else:
            self.rect.x = location[0] * 50
            self.rect.y = location[1] * 50
            return -1


class Bishop(Chessmen):
    def __init__(self, name, location, xpos, ypos):
        super().__init__()
        self.name = name
        self.location = location
        if(self.name.islower()):
            self.image = pygame.image.load(W_BISHOP)
        else:
            self.image = pygame.image.load(B_BISHOP)
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

    def moveset(self, posx, posy):
        maparr = readGame()
        pos = locationToPos(self.location)
        xoffset = abs(math.floor(posx/50) - pos[0])
        yoffset = abs(math.floor(posy/50) - pos[1])
        if xoffset == yoffset:
            return True
        else:
            return False

    def possiblemoves(self, posx, posy):
        maparr = readGame()
        if maparr[math.floor(posy/50)][math.floor(posx/50)].find("##") >= 0 and self.moveset(posx, posy):
            return True
        else:
            return False

    def enemydetect(self, posx, posy):
        maparr = readGame()
        pos = locationToPos(self.location)
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
        location = locationToPos(self.location)
        newlocation = ""

        if self.possiblemoves(posx, posy):
            writeGame(self, posx, posy)
            self.rect.x = math.floor(posx/50) * 50
            self.rect.y = math.floor(posy/50) * 50
            location[0] = math.floor(posx/50)
            location[1] = math.floor(posy/50)
            newlocation = posToLocation(location)
            self.location = newlocation
            return 0
        elif self.enemydetect(posx, posy):
            writeGame(self, posx, posy)
            self.rect.x = math.floor(posx/50) * 50
            self.rect.y = math.floor(posy/50) * 50
            location = [math.floor(posx/50), math.floor(posy/50)]
            newlocation = posToLocation(location)
            self.location = newlocation
            return 1
        else:
            self.rect.x = location[0] * 50
            self.rect.y = location[1] * 50
            return -1


class Knight(Chessmen):
    def __init__(self, name, location, xpos, ypos):
        super().__init__()
        self.name = name
        self.location = location
        if(self.name.islower()):
            self.image = pygame.image.load(W_KNIGHT)
        else:
            self.image = pygame.image.load(B_KNIGHT)
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

    def moveset(self, posx, posy):
        maparr = readGame()
        pos = locationToPos(self.location)

        if (math.floor(posy/50) == pos[1] - 2 and (math.floor(posx/50) == pos[0] - 1 or math.floor(posx/50) == pos[0] + 1)) or (math.floor(posy/50) == pos[1] + 2 and (math.floor(posx/50) == pos[0] - 1 or math.floor(posx/50) == pos[0] + 1)):
            return True
        elif (math.floor(posx/50) == pos[0] - 2 and (math.floor(posy/50) == pos[1] - 1 or math.floor(posy/50) == pos[1] + 1)) or (math.floor(posx/50) == pos[0] + 2 and (math.floor(posy/50) == pos[1] - 1 or math.floor(posy/50) == pos[1] + 1)):
            return True
        else:
            return False

    def possiblemoves(self, posx, posy):
        maparr = readGame()
        if maparr[math.floor(posy/50)][math.floor(posx/50)].find("##") >= 0 and self.moveset(posx, posy):
            return True
        else:
            return False

    def enemydetect(self, posx, posy):
        maparr = readGame()
        pos = locationToPos(self.location)
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
        location = locationToPos(self.location)
        newlocation = ""

        if self.possiblemoves(posx, posy):
            writeGame(self, posx, posy)
            self.rect.x = math.floor(posx/50) * 50
            self.rect.y = math.floor(posy/50) * 50
            location[0] = math.floor(posx/50)
            location[1] = math.floor(posy/50)
            newlocation = posToLocation(location)
            self.location = newlocation
            return 0
        elif self.enemydetect(posx, posy):
            writeGame(self, posx, posy)
            self.rect.x = math.floor(posx/50) * 50
            self.rect.y = math.floor(posy/50) * 50
            location = [math.floor(posx/50), math.floor(posy/50)]
            newlocation = posToLocation(location)
            self.location = newlocation
            return 1
        else:
            print("in else")
            self.rect.x = location[0] * 50
            self.rect.y = location[1] * 50
            return -1


class Rook(Chessmen):
    def __init__(self, name, location, xpos, ypos):
        super().__init__()
        self.name = name
        self.location = location
        if(self.name.islower()):
            self.image = pygame.image.load(W_ROOK)
        else:
            self.image = pygame.image.load(B_ROOK)
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

    def moveset(self, posx, posy):
        maparr = readGame()
        pos = locationToPos(self.location)

        if 0 <= math.floor(posx/50) <= 7 and math.floor(posy/50) == pos[1]:
            return True
        elif math.floor(posx/50) == pos[0] and 0 <= math.floor(posy/50) <= 7:
            return True
        else:
            return False

    def possiblemoves(self, posx, posy):
        maparr = readGame()
        if maparr[math.floor(posy/50)][math.floor(posx/50)].find("##") >= 0 and self.moveset(posx, posy):
            return True
        else:
            return False

    def enemydetect(self, posx, posy):
        maparr = readGame()
        pos = locationToPos(self.location)
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
        location = locationToPos(self.location)
        newlocation = ""
        if self.possiblemoves(posx, posy):
            writeGame(self, posx, posy)
            self.rect.x = math.floor(posx/50) * 50
            self.rect.y = math.floor(posy/50) * 50
            location[0] = math.floor(posx/50)
            location[1] = math.floor(posy/50)
            newlocation = posToLocation(location)
            self.location = newlocation
            return 0
        elif self.enemydetect(posx, posy):
            writeGame(self, posx, posy)
            self.rect.x = math.floor(posx/50) * 50
            self.rect.y = math.floor(posy/50) * 50
            location = [math.floor(posx/50), math.floor(posy/50)]
            newlocation = posToLocation(location)
            self.location = newlocation
            return 1
        else:
            print("in else")
            self.rect.x = location[0] * 50
            self.rect.y = location[1] * 50
            return -1


class Pawn(Chessmen):
    def __init__(self, name, location, xpos, ypos):
        super().__init__()
        self.name = name
        self.location = location
        if(self.name.islower()):
            self.image = pygame.image.load(W_PAWN)
        else:
            self.image = pygame.image.load(B_PAWN)
        self.clicked = False
        self.firstTimeMove = True
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

    def moveset(self, posx, posy):
        # x = j y = i
        maparr = readGame()
        pos = self.location
        print(pos)
        pos = locationToPos(self.location)
        if self.name.strip()[0].islower():
            if self.firstTimeMove == True and math.floor(posx/50) == pos[0] and pos[1]-2 <= math.floor(posy/50) <= pos[1]-1:
                self.firstTimeMove = False
                return True
            elif self.firstTimeMove == False and math.floor(posx/50) == pos[0] and pos[1]-1 == math.floor(posy/50):
                return True
            else:
                return False
        elif self.name.strip()[0].isupper():
            if self.firstTimeMove == True and math.floor(posx/50) == pos[0] and pos[1]+1 <= math.floor(posy/50) <= pos[1]+2:
                self.firstTimeMove = False
                return True
            elif self.firstTimeMove == False and math.floor(posx/50) == pos[0] and pos[1]+1 == math.floor(posy/50):
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
        pos = locationToPos(self.location)
        if self.name.strip()[0].islower():
            if maparr[math.floor(posy/50)][math.floor(posx/50)].split("-")[1].strip()[0].isupper():
                if (math.floor(posx/50) == pos[0]-1 or math.floor(posx/50) == pos[0]+1) and math.floor(posy/50) == pos[1]-1:
                    return True
                else:
                    return False
            else:
                return False
        elif self.name.strip()[0].isupper():
            if maparr[math.floor(posy/50)][math.floor(posx/50)].split("-")[1].strip()[0].islower():
                if (math.floor(posx/50) == pos[0]-1 or math.floor(posx/50) == pos[0]+1) and math.floor(posy/50) == pos[1]+1:
                    return True
                else:
                    return False
            else:
                return False

    def move(self, posx, posy):
        maparr = readGame()
        location = locationToPos(self.location)
        newlocation = ""

        if self.possiblemoves(posx, posy):
            writeGame(self, posx, posy)
            self.rect.x = math.floor(posx/50) * 50
            self.rect.y = math.floor(posy/50) * 50
            location[0] = math.floor(posx/50)
            location[1] = math.floor(posy/50)
            newlocation = posToLocation(location)
            self.location = newlocation
            return 0
        elif self.enemydetect(posx, posy):
            writeGame(self, posx, posy)
            self.rect.x = math.floor(posx/50) * 50
            self.rect.y = math.floor(posy/50) * 50
            location = [math.floor(posx/50), math.floor(posy/50)]
            newlocation = posToLocation(location)
            self.location = newlocation
            return 1
        else:
            print("in else")
            self.rect.x = location[0] * 50
            self.rect.y = location[1] * 50
            return -1
