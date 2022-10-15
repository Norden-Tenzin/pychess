# import numpy as np
# curr = [5, 3]
# res = [[4, 3], [6, 3], [5, 4], [5, 2], [4, 4], [4, 2], [6, 5], [6, 2]]
# pos2 = [[3, 4], [3, 6], [4, 5], [2, 5], [4, 4], [2, 4], [5, 6], [2, 6]]
# def get_dir(curr, pos):
#     # N
#     if curr[1] == pos[1] and curr[0] > pos[0]:
#         return "c-"
#     # S
#     if curr[1] == pos[1] and curr[0] < pos[0]:
#         return "c+"
#     # E
#     if curr[1] < pos[1] and curr[0] == pos[0]:
#         return "+c"
#     # W
#     if curr[1] > pos[1] and curr[0] == pos[0]:
#         return "-c"
#     # NE
#     if curr[1] < pos[1] and curr[0] > pos[0]:
#         return "+-"
#     # NW
#     if curr[1] > pos[1] and curr[0] > pos[0]:
#         return "--"
#     # SE
#     if curr[1] < pos[1] and curr[0] < pos[0]:
#         return "++"
#     # SW
#     if curr[0] < pos[0] and curr[1] > pos[1]:
#         return "-+"

# for i in res:
#     print(get_dir(curr, i))

# res = []

# for i in range(0, 8, 1):
#     temp = []
#     for j in range(0, 8, 1):
#         temp.append(tuple([i, j]))
#     res.append(temp)

# print(np.matrix(res))

curr = [2, 7]
move = [6, 4]
path = [[6, 3], [6, 2]]
pos = [0, 1]



if move in path: 
    print("yes")
else:
    print("no")

def make_obj(openSpace, hit):
    d = dict()
    d['open'] = openSpace
    d['hit'] = hit
    return d

make_obj([[1,2], [1,3]], [[2,4], [4,5]])
make_obj([], [[2,4], [4,5]])
make_obj([[1,2], [1,3]], [])

def test():
    return 1, 2, True, False
print(type(test()))

{
    'n': {'open': [[6, 4], [5, 4], [4, 4], [3, 4], [2, 4], [1, 4]], 'hit': [0, 4]}, 
    'e': {'open': [], 'hit': []}, 
    'w': {'open': [], 'hit': []}, 
    's': {'open': [], 'hit': []}, 
    'ne': {'open': [[6, 5], [5, 6], [4, 7]], 'hit': []}, 
    'nw': {'open': [[6, 3], [5, 2], [4, 1], [3, 0]], 'hit': []}, 
    'se': {'open': [], 'hit': []}, 'sw': {'open': [], 'hit': []}
}