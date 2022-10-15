from helper_functions import *

# Chess Piece
class Chessmen(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
    
    def make_obj(self, openSpace, hit):
        d = dict()
        d['open'] = openSpace
        d['hit'] = hit
        return d

# King
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

    def clear_path(self, direction, currx, curry, maparr, curr_path):
        def get_increment(direction, currx, curry):
            def add_using_symb(symb, val1, val2):
                if symb == "+":
                    return val1 + val2
                elif symb == "-":
                    return val1 - val2
                elif symb == "c": 
                    return val1
            x_symb, y_symb = direction[0], direction[1]
            return add_using_symb(x_symb, currx, CELLSIZE), add_using_symb(y_symb, curry, CELLSIZE)
        currx, curry = get_increment(direction, currx, curry)
        if not (0 <= currx < SIZE and 0 <= curry < SIZE):
            return self.make_obj(curr_path, [])
        else:
            if maparr[math.floor(curry/50)][math.floor(currx/50)].find("##") >= 0:
                curr_path.append([math.floor(curry/50), math.floor(currx/50)])
                return self.make_obj(curr_path, [])
            else:
                hit = maparr[math.floor(curry/50)][math.floor(currx/50)].split("-")[1]
                # curr is a black_piece
                if any(ele.isupper() for ele in self.name):
                    # and hit is a black_piece
                    if any(ele.isupper() for ele in hit):
                        return self.make_obj(curr_path, [])
                    # and hit is white piece
                    else:
                        return self.make_obj(curr_path, [math.floor(curry/50), math.floor(currx/50)])
                # curr is a white_piece
                else:
                    if any(ele.isupper() for ele in hit):
                        return self.make_obj(curr_path, [math.floor(curry/50), math.floor(currx/50)])
                    else:
                        return self.make_obj(curr_path, [])

    def clear_paths(self, posx, posy, playAs, maparr):
        currx, curry = math.floor(posx/50)*CELLSIZE, math.floor(posy/50)*CELLSIZE

        # vertiacl
        # vertical pos to North c-
        n_path = self.clear_path("c-", currx, curry, maparr, [])
        # print(" PATH: {}".format(n_path))

        # vertical pos to East +c
        e_path = self.clear_path("+c", currx, curry, maparr, [])
        # print(" PATH: {}".format(e_path))

        # vertical pos to West -c
        w_path = self.clear_path("-c", currx, curry, maparr, [])
        # print(" PATH: {}".format(w_path))

        # vertical pos to South c+
        s_path = self.clear_path("c+", currx, curry, maparr, [])
        # print(" PATH: {}".format(s_path))

        # diagonal
        # diagonal pos to North East +-
        ne_path = self.clear_path("+-", currx, curry, maparr, [])
        # print("NE PATH: {}".format(ne_path))

        # diagonal pos to North West --
        nw_path = self.clear_path("--", currx, curry, maparr, [])
        # print("NW PATH: {}".format(nw_path))

        # diagonal pos to South East ++
        se_path = self.clear_path("++", currx, curry, maparr, [])
        # print("SE PATH: {}".format(se_path))

        # diagonal pos to South West -+
        sw_path = self.clear_path("-+", currx, curry, maparr, [])
        # print("SW PATH: {}".format(sw_path))

        return ({
            "n" : n_path,
            "e" : e_path,
            "w" : w_path,
            "s" : s_path,
            "ne": ne_path,
            "nw": nw_path,
            "se": se_path,
            "sw": sw_path
        }, (currx, curry))

    def move_set(self, posx, posy, maparr):
        for i, line in enumerate(maparr):
            for j, tile in enumerate(line):
                if tile.split("-")[1] == self.name:
                    if j-1 <= math.floor(posx/50) <= j+1 and i-1 <= math.floor(posy/50) <= i+1:
                        return True
                    else:
                        return False

    def possible_moves(self, posx, posy, maparr):
        if maparr[math.floor(posy/50)][math.floor(posx/50)].find("##") >= 0 and self.move_set(posx, posy, maparr):
            return True
        else:
            return False

    def enemy_detect(self, posx, posy, maparr):  # if the enemy is on that pos
        if self.name.strip()[0].islower():
            if maparr[math.floor(posy/50)][math.floor(posx/50)].split("-")[1].strip()[0].isupper() and self.move_set(posx, posy, maparr):
                return True
            else:
                return False
        elif self.name.strip()[0].isupper():
            if maparr[math.floor(posy/50)][math.floor(posx/50)].split("-")[1].strip()[0].islower() and self.move_set(posx, posy, maparr):
                return True
            else:
                return False

    def move(self, posx, posy, maparr):
        pos = location_to_pos(self.location)

        # case when the piece isnt moved from its curr pos
        if math.floor(posx/CELLSIZE) == pos[1] and math.floor(posy/CELLSIZE) == pos[0]:
            return (-1, maparr, True)
            
        if self.possible_moves(posx, posy, maparr):
            maparr = writeGame(self, posx, posy, maparr)
            self.rect.x = math.floor(posx/50) * 50
            self.rect.y = math.floor(posy/50) * 50
            pos = [math.floor(posy/50), math.floor(posx/50)]
            newlocation = pos_to_location(pos)
            self.location = newlocation
            return (0, maparr, False)
        elif self.enemy_detect(posx, posy, maparr):
            maparr = writeGame(self, posx, posy, maparr)
            self.rect.x = math.floor(posx/50) * 50
            self.rect.y = math.floor(posy/50) * 50
            pos = [math.floor(posy/50), math.floor(posx/50)]
            newlocation = pos_to_location(pos)
            self.location = newlocation
            return (1, maparr, False)
        else:
            self.rect.x = pos[1] * 50
            self.rect.y = pos[0] * 50
            return (-1, maparr, True)

# Queen
class Queen(Chessmen):
    def __init__(self, name, location, xpos, ypos):
        super().__init__()
        self.clicked = False
        self.name = name
        self.location = location
        if(self.name.islower()):
            self.image = pygame.image.load(W_QUEEN)
        else:
            self.image = pygame.image.load(B_QUEEN)
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

    def clear_path(self, direction, currx, curry, maparr, curr_path):
        def get_increment(direction, currx, curry):
            def add_using_symb(symb, val1, val2):
                if symb == "+":
                    return val1 + val2
                elif symb == "-":
                    return val1 - val2
                elif symb == "c": 
                    return val1
            x_symb, y_symb = direction[0], direction[1]
            return add_using_symb(x_symb, currx, CELLSIZE), add_using_symb(y_symb, curry, CELLSIZE)
        currx, curry = get_increment(direction, currx, curry)
        if not (0 <= currx < SIZE and 0 <= curry < SIZE):
            return self.make_obj(curr_path, [])
        else:
            if maparr[math.floor(curry/50)][math.floor(currx/50)].find("##") >= 0:
                curr_path.append([math.floor(curry/50), math.floor(currx/50)])
                return self.clear_path(direction, currx, curry, maparr, curr_path)
            else:
                hit = maparr[math.floor(curry/50)][math.floor(currx/50)].split("-")[1]
                # curr is a black_piece
                if any(ele.isupper() for ele in self.name):
                    # and hit is a black_piece
                    if any(ele.isupper() for ele in hit):
                        return self.make_obj(curr_path, [])
                    else:
                        return self.make_obj(curr_path, [[math.floor(curry/50), math.floor(currx/50)]])
                # curr is a white_piece
                else:
                    if any(ele.isupper() for ele in hit):
                        return self.make_obj(curr_path, [[math.floor(curry/50), math.floor(currx/50)]])
                    else:
                        return self.make_obj(curr_path, [])

    def clear_paths(self, posx, posy, playAs, maparr):
        currx, curry = math.floor(posx/50)*CELLSIZE, math.floor(posy/50)*CELLSIZE

        # vertiacl
        # vertical pos to North c-
        n_path = self.clear_path("c-", currx, curry, maparr, [])
        # print(" PATH: {}".format(n_path))

        # vertical pos to East +c
        e_path = self.clear_path("+c", currx, curry, maparr, [])
        # print(" PATH: {}".format(e_path))

        # vertical pos to West -c
        w_path = self.clear_path("-c", currx, curry, maparr, [])
        # print(" PATH: {}".format(w_path))

        # vertical pos to South c+
        s_path = self.clear_path("c+", currx, curry, maparr, [])
        # print(" PATH: {}".format(s_path))

        # diagonal
        # diagonal pos to North East +-
        ne_path = self.clear_path("+-", currx, curry, maparr, [])
        # print("NE PATH: {}".format(ne_path))

        # diagonal pos to North West --
        nw_path = self.clear_path("--", currx, curry, maparr, [])
        # print("NW PATH: {}".format(nw_path))

        # diagonal pos to South East ++
        se_path = self.clear_path("++", currx, curry, maparr, [])
        # print("SE PATH: {}".format(se_path))

        # diagonal pos to South West -+
        sw_path = self.clear_path("-+", currx, curry, maparr, [])
        # print("SW PATH: {}".format(sw_path))

        return ({
            "n" : n_path,
            "e" : e_path,
            "w" : w_path,
            "s" : s_path,
            "ne": ne_path,
            "nw": nw_path,
            "se": se_path,
            "sw": sw_path
        }, (currx, curry))

    def move_set(self, posx, posy, maparr):
        pos = location_to_pos(self.location)
        xoffset = abs(math.floor(posx/50) - pos[1])
        yoffset = abs(math.floor(posy/50) - pos[0])

        if 0 <= math.floor(posx/50) <= 7 and math.floor(posy/50) == pos[0]:
            return True
        elif math.floor(posx/50) == pos[1] and 0 <= math.floor(posy/50) <= 7:
            return True
        elif xoffset == yoffset:
            return True
        else:
            return False

    def possible_moves(self, posx, posy, maparr):
        def get_dir(curr, pos):
            # N
            if curr[1] == pos[1] and curr[0] > pos[0]:
                return "c-"
            # S
            if curr[1] == pos[1] and curr[0] < pos[0]:
                return "c+"
            # E
            if curr[1] < pos[1] and curr[0] == pos[0]:
                return "+c"
            # W
            if curr[1] > pos[1] and curr[0] == pos[0]:
                return "-c"
            # NE
            if curr[1] < pos[1] and curr[0] > pos[0]:
                return "+-"
            # NW
            if curr[1] > pos[1] and curr[0] > pos[0]:
                return "--"
            # SE
            if curr[1] < pos[1] and curr[0] < pos[0]:
                return "++"
            # SW
            if curr[0] < pos[0] and curr[1] > pos[1]:
                return "-+"
            # STATIC
            if curr[0] == pos[0] and curr[1] == pos[1]:
                return "cc"
        
        curry, currx = location_to_pos(self.location)
        direction = get_dir([curry, currx], [math.floor(posy/50), math.floor(posx/50)])
        path = self.clear_path(direction, currx*CELLSIZE, curry*CELLSIZE, maparr, [])['open']
        if maparr[math.floor(posy/50)][math.floor(posx/50)].find("##") >= 0 and self.move_set(posx, posy, maparr) and [math.floor(posy/50), math.floor(posx/50)] in path:
            return True
        else:
            return False

    def enemy_detect(self, posx, posy, maparr):
        if self.name.strip()[0].islower():
            if maparr[math.floor(posy/50)][math.floor(posx/50)].split("-")[1].strip()[0].isupper() and self.move_set(posx, posy, maparr):
                return True
            else:
                return False
        elif self.name.strip()[0].isupper():
            if maparr[math.floor(posy/50)][math.floor(posx/50)].split("-")[1].strip()[0].islower() and self.move_set(posx, posy, maparr):
                return True
            else:
                return False

    def move(self, posx, posy, maparr):
        pos = location_to_pos(self.location)

        # case when the piece isnt moved from its curr pos
        if math.floor(posx/CELLSIZE) == pos[1] and math.floor(posy/CELLSIZE) == pos[0]:
            return (-1, maparr, True)

        if self.possible_moves(posx, posy, maparr):
            writeGame(self, posx, posy, maparr)
            self.rect.x = math.floor(posx/50) * 50
            self.rect.y = math.floor(posy/50) * 50
            pos = [math.floor(posy/50), math.floor(posx/50)]
            newlocation = pos_to_location(pos)
            self.location = newlocation
            return (0, maparr, False)
        elif self.enemy_detect(posx, posy, maparr):
            writeGame(self, posx, posy, maparr)
            self.rect.x = math.floor(posx/50) * 50
            self.rect.y = math.floor(posy/50) * 50
            pos = [math.floor(posy/50), math.floor(posx/50)]
            newlocation = pos_to_location(pos)
            self.location = newlocation
            return (1, maparr, False)
        else:
            self.rect.x = pos[1] * 50
            self.rect.y = pos[0] * 50
            return (-1, maparr, True)

# Bishop
class Bishop(Chessmen):
    def __init__(self, name, location, xpos, ypos):
        super().__init__()
        self.clicked = False
        self.name = name
        self.location = location
        if(self.name.islower()):
            self.image = pygame.image.load(W_BISHOP)
        else:
            self.image = pygame.image.load(B_BISHOP)
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

    def clear_path(self, direction, currx, curry, maparr, curr_path):
        def get_increment(direction, currx, curry):
            def add_using_symb(symb, val1, val2):
                if symb == "+":
                    return val1 + val2
                elif symb == "-":
                    return val1 - val2
                elif symb == "c": 
                    return val1
            x_symb, y_symb = direction[0], direction[1]
            return add_using_symb(x_symb, currx, CELLSIZE), add_using_symb(y_symb, curry, CELLSIZE)
        currx, curry = get_increment(direction, currx, curry)
        if not (0 <= currx < SIZE and 0 <= curry < SIZE):
            return self.make_obj(curr_path, [])
        else:
            if maparr[math.floor(curry/50)][math.floor(currx/50)].find("##") >= 0:
                curr_path.append([math.floor(curry/50), math.floor(currx/50)])
                return self.clear_path(direction, currx, curry, maparr, curr_path)
            else:
                hit = maparr[math.floor(curry/50)][math.floor(currx/50)].split("-")[1]
                # curr is a black_piece
                if any(ele.isupper() for ele in self.name):
                    # and hit is a black_piece
                    if any(ele.isupper() for ele in hit):
                        return self.make_obj(curr_path, [])
                    else:
                        return self.make_obj(curr_path, [[math.floor(curry/50), math.floor(currx/50)]])
                # curr is a white_piece
                else:
                    if any(ele.isupper() for ele in hit):
                        return self.make_obj(curr_path, [[math.floor(curry/50), math.floor(currx/50)]])
                    else:
                        return self.make_obj(curr_path, [])

    def clear_paths(self, posx, posy, playAs, maparr):
        currx, curry = math.floor(posx/50)*CELLSIZE, math.floor(posy/50)*CELLSIZE
        # diagonal pos to North East +-
        ne_path = self.clear_path("+-", currx, curry, maparr, [])
        # print("NE PATH: {}".format(ne_path))

        # diagonal pos to North West --
        nw_path = self.clear_path("--", currx, curry, maparr, [])
        # print("NW PATH: {}".format(nw_path))

        # diagonal pos to South East ++
        se_path = self.clear_path("++", currx, curry, maparr, [])
        # print("SE PATH: {}".format(se_path))

        # diagonal pos to South West -+
        sw_path = self.clear_path("-+", currx, curry, maparr, [])
        # print("SW PATH: {}".format(sw_path))

        return ({
            "ne": ne_path,
            "nw": nw_path,
            "se": se_path,
            "sw": sw_path
        }, (currx, curry))
        
    def move_set(self, posx, posy):
        pos = location_to_pos(self.location)
        xoffset = abs(math.floor(posx/50) - pos[1])
        yoffset = abs(math.floor(posy/50) - pos[0])
        if xoffset == yoffset:
            return True
        else:
            return False

    def possible_moves(self, posx, posy, maparr):
        def get_dir(curr, pos):
            # N
            if curr[1] == pos[1] and curr[0] > pos[0]:
                return "c-"
            # S
            if curr[1] == pos[1] and curr[0] < pos[0]:
                return "c+"
            # E
            if curr[1] < pos[1] and curr[0] == pos[0]:
                return "+c"
            # W
            if curr[1] > pos[1] and curr[0] == pos[0]:
                return "-c"
            # NE
            if curr[1] < pos[1] and curr[0] > pos[0]:
                return "+-"
            # NW
            if curr[1] > pos[1] and curr[0] > pos[0]:
                return "--"
            # SE
            if curr[1] < pos[1] and curr[0] < pos[0]:
                return "++"
            # SW
            if curr[0] < pos[0] and curr[1] > pos[1]:
                return "-+"
            
            # STATIC
            if curr[0] == pos[0] and curr[1] == pos[1]:
                return "cc"
        
        curry, currx = location_to_pos(self.location)
        direction = get_dir([curry, currx], [math.floor(posy/50), math.floor(posx/50)])
        path = self.clear_path(direction, currx*CELLSIZE, curry*CELLSIZE, maparr, [])['open']

        if maparr[math.floor(posy/50)][math.floor(posx/50)].find("##") >= 0 and self.move_set(posx, posy) and [math.floor(posy/50), math.floor(posx/50)] in path:
            return True
        else:
            return False

    def enemy_detect(self, posx, posy, maparr):
        if self.name.strip()[0].islower():
            if maparr[math.floor(posy/50)][math.floor(posx/50)].split("-")[1].strip()[0].isupper() and self.move_set(posx, posy):
                return True
            else:
                return False
        elif self.name.strip()[0].isupper():
            if maparr[math.floor(posy/50)][math.floor(posx/50)].split("-")[1].strip()[0].islower() and self.move_set(posx, posy):
                return True
            else:
                return False

    def move(self, posx, posy, maparr):
        pos = location_to_pos(self.location)

        # case when the piece isnt moved from its curr pos
        if math.floor(posx/CELLSIZE) == pos[1] and math.floor(posy/CELLSIZE) == pos[0]:
            return (-1, maparr, True)

        if self.possible_moves(posx, posy, maparr):
            writeGame(self, posx, posy, maparr)
            self.rect.x = math.floor(posx/50) * 50
            self.rect.y = math.floor(posy/50) * 50
            pos = [math.floor(posy/50), math.floor(posx/50)]
            newlocation = pos_to_location(pos)
            self.location = newlocation
            return (0, maparr, False)
        elif self.enemy_detect(posx, posy, maparr):
            writeGame(self, posx, posy, maparr)
            self.rect.x = math.floor(posx/50) * 50
            self.rect.y = math.floor(posy/50) * 50
            pos = [math.floor(posy/50), math.floor(posx/50)]
            newlocation = pos_to_location(pos)
            self.location = newlocation
            return (1, maparr, False)
        else:
            self.rect.x = pos[1] * 50
            self.rect.y = pos[0] * 50
            return (-1, maparr, True)

# Knight
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

    def clear_path(self, direction, currx, curry, maparr, curr_path):
        def validPos(pos1, pos2):
            def check(curr):
                currx, curry = curr
                if not (0 <= currx < SIZE and 0 <= curry < SIZE):
                    return self.make_obj([], [])
                else:
                    if maparr[math.floor(curry/50)][math.floor(currx/50)].find("##") >= 0:
                        return self.make_obj([math.floor(curry/50), math.floor(currx/50)], [])
                    else:
                        hit = maparr[math.floor(curry/50)][math.floor(currx/50)].split("-")[1]
                        # curr is a black_piece
                        if any(ele.isupper() for ele in self.name):
                            # and hit is a black_piece
                            if any(ele.isupper() for ele in hit):
                                return self.make_obj([], [])
                            else:
                                return self.make_obj([], [math.floor(curry/50), math.floor(currx/50)])
                        # curr is a white_piece
                        else:
                            if any(ele.isupper() for ele in hit):
                                return self.make_obj([], [math.floor(curry/50), math.floor(currx/50)])
                            else:
                                return self.make_obj([], [])

            resLeft = check(pos1)
            resRight  = check(pos2)

            res = self.make_obj([x for x in [resLeft['open'],resRight['open']] if x != []], [x for x in [resLeft['hit'],resRight['hit']]if x != []])
            return res
            
        # def get_increment(direction, currx, curry):
        #     def add_using_symb(symb, val1, val2):
        #         if symb == "up"
        #     x_symb, y_symb = direction[0], direction[1]
        #     return add_using_symb(x_symb, currx, CELLSIZE), add_using_symb(y_symb, curry, CELLSIZE)
        # currx, curry = get_increment(direction, currx, curry)

        if direction == "up":
            left = [currx - (1*CELLSIZE), curry - (2*CELLSIZE)]
            right = [currx + (1*CELLSIZE), curry - (2*CELLSIZE)]
            return validPos(left, right)

        elif direction == "dp":
            left = [currx - (1*CELLSIZE), curry + (2*CELLSIZE)]
            right = [currx + (1*CELLSIZE), curry + (2*CELLSIZE)]
            return validPos(left, right)
        
        elif direction == "lp":
            up = [currx - (2*CELLSIZE), curry - (1*CELLSIZE)]
            down = [currx - (2*CELLSIZE), curry + (1*CELLSIZE)]
            return validPos(up, down)

        elif direction == "rp":
            up = [currx + (2*CELLSIZE), curry - (1*CELLSIZE)]
            down = [currx + (2*CELLSIZE), curry + (1*CELLSIZE)]
            return validPos(up, down)

        return self.make_obj([], [])
        
    def clear_paths(self, posx, posy, playAs, maparr):
        currx, curry = math.floor(posx/50)*CELLSIZE, math.floor(posy/50)*CELLSIZE
        
        # up
        u_path = self.clear_path("up", currx, curry, maparr, [])
        
        # down
        d_path = self.clear_path("dp", currx, curry, maparr, [])
        
        # left
        l_path = self.clear_path("lp", currx, curry, maparr, [])
        
        # right
        r_path = self.clear_path("rp", currx, curry, maparr, [])

        return ({
            "n" : u_path,
            "e" : r_path,
            "w" : l_path,
            "s" : d_path,
        }, (currx, curry))

    def move_set(self, posx, posy, maparr):
        pos = location_to_pos(self.location)

        if (math.floor(posy/50) == pos[0] - 2 and (math.floor(posx/50) == pos[1] - 1 or math.floor(posx/50) == pos[1] + 1)) or (math.floor(posy/50) == pos[0] + 2 and (math.floor(posx/50) == pos[1] - 1 or math.floor(posx/50) == pos[1] + 1)):
            return True
        elif (math.floor(posx/50) == pos[1] - 2 and (math.floor(posy/50) == pos[0] - 1 or math.floor(posy/50) == pos[0] + 1)) or (math.floor(posx/50) == pos[1] + 2 and (math.floor(posy/50) == pos[0] - 1 or math.floor(posy/50) == pos[0] + 1)):
            return True
        else:
            return False

    def possible_moves(self, posx, posy, maparr):
        if maparr[math.floor(posy/50)][math.floor(posx/50)].find("##") >= 0 and self.move_set(posx, posy, maparr):
            return True
        else:
            return False

    def enemy_detect(self, posx, posy, maparr):
        if self.name.strip()[0].islower():
            if maparr[math.floor(posy/50)][math.floor(posx/50)].split("-")[1].strip()[0].isupper() and self.move_set(posx, posy, maparr):
                return True
            else:
                return False
        elif self.name.strip()[0].isupper():
            if maparr[math.floor(posy/50)][math.floor(posx/50)].split("-")[1].strip()[0].islower() and self.move_set(posx, posy, maparr):
                return True
            else:
                return False
    
    def move(self, posx, posy, maparr):
        pos = location_to_pos(self.location)

        # case when the piece isnt moved from its curr pos
        if math.floor(posx/CELLSIZE) == pos[1] and math.floor(posy/CELLSIZE) == pos[0]:
            return (-1, maparr, True)

        if self.possible_moves(posx, posy, maparr):
            writeGame(self, posx, posy, maparr)
            self.rect.x = math.floor(posx/50) * 50
            self.rect.y = math.floor(posy/50) * 50
            pos = [math.floor(posy/50), math.floor(posx/50)]
            newlocation = pos_to_location(pos)
            self.location = newlocation
            return (0, maparr, False)
        elif self.enemy_detect(posx, posy, maparr):
            writeGame(self, posx, posy, maparr)
            self.rect.x = math.floor(posx/50) * 50
            self.rect.y = math.floor(posy/50) * 50
            pos = [math.floor(posy/50), math.floor(posx/50)]
            newlocation = pos_to_location(pos)
            self.location = newlocation
            return (1, maparr, False)
        else:
            self.rect.x = pos[1] * 50
            self.rect.y = pos[0] * 50
            return (-1, maparr, True)

# Rook
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

    def clear_path(self, direction, currx, curry, maparr, curr_path):
        def get_increment(direction, currx, curry):
            def add_using_symb(symb, val1, val2):
                if symb == "+":
                    return val1 + val2
                elif symb == "-":
                    return val1 - val2
                elif symb == "c": 
                    return val1
            x_symb, y_symb = direction[0], direction[1]
            return add_using_symb(x_symb, currx, CELLSIZE), add_using_symb(y_symb, curry, CELLSIZE)
        currx, curry = get_increment(direction, currx, curry)
        if not (0 <= currx < SIZE and 0 <= curry < SIZE):
            return self.make_obj(curr_path, [])
        else:
            if maparr[math.floor(curry/50)][math.floor(currx/50)].find("##") >= 0:
                curr_path.append([math.floor(curry/50), math.floor(currx/50)])
                return self.clear_path(direction, currx, curry, maparr, curr_path)
            else:
                hit = maparr[math.floor(curry/50)][math.floor(currx/50)].split("-")[1]
                # curr is a black_piece
                if any(ele.isupper() for ele in self.name):
                    # and hit is a black_piece
                    if any(ele.isupper() for ele in hit):
                        return self.make_obj(curr_path, [])
                    else:
                        return self.make_obj(curr_path, [[math.floor(curry/50), math.floor(currx/50)]])
                # curr is a white_piece
                else:
                    if any(ele.isupper() for ele in hit):
                        return self.make_obj(curr_path, [[math.floor(curry/50), math.floor(currx/50)]])
                    else:
                        return self.make_obj(curr_path, [])

    def clear_paths(self, posx, posy, playAs, maparr):
        currx, curry = math.floor(posx/50)*CELLSIZE, math.floor(posy/50)*CELLSIZE

        # vertiacl
        # vertical pos to North c-
        n_path = self.clear_path("c-", currx, curry, maparr, [])
        # print(" PATH: {}".format(n_path))

        # vertical pos to East +c
        e_path = self.clear_path("+c", currx, curry, maparr, [])
        # print(" PATH: {}".format(e_path))

        # vertical pos to West -c
        w_path = self.clear_path("-c", currx, curry, maparr, [])
        # print(" PATH: {}".format(w_path))

        # vertical pos to South c+
        s_path = self.clear_path("c+", currx, curry, maparr, [])
        # print(" PATH: {}".format(s_path))

        return ({
            "n" : n_path,
            "e" : e_path,
            "w" : w_path,
            "s" : s_path,
        }, (currx, curry))

    def move_set(self, posx, posy):
        pos = location_to_pos(self.location)

        if 0 <= math.floor(posx/50) <= 7 and math.floor(posy/50) == pos[0]:
            return True
        elif math.floor(posx/50) == pos[1] and 0 <= math.floor(posy/50) <= 7:
            return True
        else:
            return False

    def possible_moves(self, posx, posy, maparr):
        def get_dir(curr, pos):
            # N
            if curr[1] == pos[1] and curr[0] > pos[0]:
                return "c-"
            # S
            if curr[1] == pos[1] and curr[0] < pos[0]:
                return "c+"
            # E
            if curr[1] < pos[1] and curr[0] == pos[0]:
                return "+c"
            # W
            if curr[1] > pos[1] and curr[0] == pos[0]:
                return "-c"
            # NE
            if curr[1] < pos[1] and curr[0] > pos[0]:
                return "+-"
            # NW
            if curr[1] > pos[1] and curr[0] > pos[0]:
                return "--"
            # SE
            if curr[1] < pos[1] and curr[0] < pos[0]:
                return "++"
            # SW
            if curr[0] < pos[0] and curr[1] > pos[1]:
                return "-+"
            # STATIC
            if curr[0] == pos[0] and curr[1] == pos[1]:
                return "cc"
        
        curry, currx = location_to_pos(self.location)
        direction = get_dir([curry, currx], [math.floor(posy/50), math.floor(posx/50)])
        path = self.clear_path(direction, currx*CELLSIZE, curry*CELLSIZE, maparr, [])['open']
        if maparr[math.floor(posy/50)][math.floor(posx/50)].find("##") >= 0 and self.move_set(posx, posy) and [math.floor(posy/50), math.floor(posx/50)] in path:
            return True
        else:
            return False

    def enemy_detect(self, posx, posy, maparr):
        if self.name.strip()[0].islower():
            if maparr[math.floor(posy/50)][math.floor(posx/50)].split("-")[1].strip()[0].isupper() and self.move_set(posx, posy):
                return True
            else:
                return False
        elif self.name.strip()[0].isupper():
            if maparr[math.floor(posy/50)][math.floor(posx/50)].split("-")[1].strip()[0].islower() and self.move_set(posx, posy):
                return True
            else:
                return False

    def move(self, posx, posy, maparr):
        pos = location_to_pos(self.location)

        # case when the piece isnt moved from its curr pos
        if math.floor(posx/CELLSIZE) == pos[1] and math.floor(posy/CELLSIZE) == pos[0]:
            return (-1, maparr, True)

        if self.possible_moves(posx, posy, maparr):
            writeGame(self, posx, posy, maparr)
            self.rect.x = math.floor(posx/50) * 50
            self.rect.y = math.floor(posy/50) * 50
            pos = [math.floor(posy/50), math.floor(posx/50)]
            newlocation = pos_to_location(pos)
            self.location = newlocation
            return (0, maparr, False)
        elif self.enemy_detect(posx, posy, maparr):
            writeGame(self, posx, posy, maparr)
            self.rect.x = math.floor(posx/50) * 50
            self.rect.y = math.floor(posy/50) * 50
            pos = [math.floor(posy/50), math.floor(posx/50)]
            newlocation = pos_to_location(pos)
            self.location = newlocation
            return (1, maparr, False)
        else:
            self.rect.x = pos[1] * 50
            self.rect.y = pos[0] * 50
            return (-1, maparr, True)

# Pawn
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

    def clear_path(self, direction, currx, curry, increment, maparr, curr_path):
        def first_step(currx, curry, curr_path):
            hit_lst = []
            if maparr[curry][currx].find("##") >= 0:
                curr_path.append([curry, currx])

            # left
            l_hit = [curry, currx-1]
            if (0 <= l_hit[0] < INDEXSIZE and 0 <= l_hit[1] < INDEXSIZE):
                # print("INSIDE L_HIT")
                if maparr[l_hit[0]][l_hit[1]].find("##") < 0:
                    hit = maparr[l_hit[0]][l_hit[1]].split("-")[1]
                    # curr is a black_piece
                    if any(ele.isupper() for ele in self.name):
                        # and hit is a black_piece
                        if any(ele.isupper() for ele in hit):
                            pass
                        # and hit is white piece
                        else:
                            hit_lst.append([l_hit[0], l_hit[1]])
                    # curr is a white_piece
                    else:
                        if any(ele.isupper() for ele in hit):
                            hit_lst.append([l_hit[0], l_hit[1]])
                        else:
                            pass
            
            # right
            r_hit = [curry, currx+1]
            if (0 <= r_hit[0] < INDEXSIZE and 0 <= r_hit[1] < INDEXSIZE):
                # print("INSIDE R_HIT")
                if maparr[r_hit[0]][r_hit[1]].find("##") < 0:
                    hit = maparr[r_hit[0]][r_hit[1]].split("-")[1]
                    # curr is a black_piece
                    if any(ele.isupper() for ele in self.name):
                        # and hit is a black_piece
                        if any(ele.isupper() for ele in hit):
                            pass
                        # and hit is white piece
                        else:
                            hit_lst.append([r_hit[0], r_hit[1]])
                    # curr is a white_piece
                    else:
                        if any(ele.isupper() for ele in hit):
                            hit_lst.append([r_hit[0], r_hit[1]])
                        else:
                            pass
            return curr_path, hit_lst

        def second_step(currx, curry, curr_path):
            if maparr[curry][currx].find("##") >= 0:
                curr_path.append([curry, currx])
            return curr_path
    
        if not (0 <= currx < INDEXSIZE and 0 <= curry < INDEXSIZE):
            return self.make_obj(curr_path, [])
        else:
            if self.firstTimeMove:
                curr_path, hit_lst = first_step(currx, curry, curr_path)
                curr_path = second_step(currx, curry + increment, curr_path)
                return self.make_obj(curr_path, hit_lst)
            else:
                curr_path, hit_lst = first_step(currx, curry, curr_path)
                return self.make_obj(curr_path, hit_lst)

    def clear_paths(self, posx, posy, playAs, maparr):
        currx, curry = math.floor(posx/50), math.floor(posy/50)

        # playing as white
        if playAs == 0:
            if self.name[0].islower():
                path = self.clear_path("c-", currx, curry-1, -1, maparr, [])
            else:
                path = self.clear_path("c-", currx, curry+1, 1, maparr, [])
        elif playAs == 1:
            if self.name[0].upper():
                path = self.clear_path("c-", currx, curry-1, -1, maparr, [])
            else:
                path = self.clear_path("c-", currx, curry+1, 1, maparr, [])

        return ({
            "p" : path,
        }, (currx*CELLSIZE, curry*CELLSIZE))

    def move_set(self, posx, posy, maparr):
        pos = self.location
        pos = location_to_pos(self.location)
        if self.name.strip()[0].islower():
            if self.firstTimeMove == True and math.floor(posx/50) == pos[1] and pos[0]-2 <= math.floor(posy/50) <= pos[0]-1:
                self.firstTimeMove = False
                return True
            elif self.firstTimeMove == False and math.floor(posx/50) == pos[1] and pos[0]-1 == math.floor(posy/50):
                return True
            else:
                return False
        elif self.name.strip()[0].isupper():
            if self.firstTimeMove == True and math.floor(posx/50) == pos[1] and pos[0]+1 <= math.floor(posy/50) <= pos[0]+2:
                self.firstTimeMove = False
                return True
            elif self.firstTimeMove == False and math.floor(posx/50) == pos[1] and pos[0]+1 == math.floor(posy/50):
                return True
            else:
                return False

    def possible_moves(self, posx, posy, maparr):
        if maparr[math.floor(posy/50)][math.floor(posx/50)].find("##") >= 0 and self.move_set(posx, posy, maparr):
            return True
        else:
            return False

    def enemy_detect(self, posx, posy, maparr):  
        pos = location_to_pos(self.location)

        # if piece is white
        if self.name.strip()[0].islower():
            if maparr[math.floor(posy/50)][math.floor(posx/50)].split("-")[1].strip()[0].isupper():
                if (math.floor(posx/50) == pos[1]-1 or math.floor(posx/50) == pos[1]+1) and math.floor(posy/50) == pos[0]-1:
                    return True
                else:
                    return False
            else:
                return False
        # if piece is black
        elif self.name.strip()[0].isupper():
            if maparr[math.floor(posy/50)][math.floor(posx/50)].split("-")[1].strip()[0].islower():
                if (math.floor(posx/50) == pos[1]-1 or math.floor(posx/50) == pos[1]+1) and math.floor(posy/50) == pos[0]+1:
                    return True
                else:
                    return False
            else:
                return False

    def move(self, posx, posy, maparr):
        pos = location_to_pos(self.location)
        # print(math.floor(posy/CELLSIZE), math.floor(posx/CELLSIZE))
        # print(pos)

        # case when the piece isnt moved from its curr pos
        if math.floor(posx/CELLSIZE) == pos[1] and math.floor(posy/CELLSIZE) == pos[0]:
            return (-1, maparr, True)
        
        # case when the piece is moved
        if self.possible_moves(posx, posy, maparr):
            maparr = writeGame(self, posx, posy, maparr)
            self.rect.x = math.floor(posx/50) * 50
            self.rect.y = math.floor(posy/50) * 50
            pos = [math.floor(posy/50), math.floor(posx/50)]
            newlocation = pos_to_location(pos)
            self.location = newlocation
            return (0, maparr, False)
        elif self.enemy_detect(posx, posy, maparr):
            maparr = writeGame(self, posx, posy, maparr)
            self.rect.x = math.floor(posx/50) * 50
            self.rect.y = math.floor(posy/50) * 50
            pos = [math.floor(posy/50), math.floor(posx/50)]
            newlocation = pos_to_location(pos)
            self.location = newlocation
            return (1, maparr, False)
        else:
            self.rect.x = pos[1] * 50
            self.rect.y = pos[0] * 50
            return (-1, maparr, True)
