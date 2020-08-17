import string
import numpy as np
from constants import *

alphabetsoup = list(map(chr, range(97, 105)))
blackpieces = ["Ro", "Kn", "Bi", "Qu", "Ki", "Bi", "Kn",
               "Ro", "Pa", "Pa", "Pa", "Pa", "Pa", "Pa", "Pa", "Pa"]
whitepieces = ["pa", "pa", "pa", "pa", "pa", "pa", "pa",
               "pa", "ro", "kn", "bi", "qu", "ki", "bi", "kn", "ro"]


def main():
    oneList = ""
    oneBoard = []

    for x in range(8, 0, -1):
        for i, y in enumerate(alphabetsoup):
            print(x, y)
            if x == 8:
                oneList = (oneList + y + str(x) + "-" +
                           str(blackpieces[i]) + ",")
            elif x == 7:
                oneList = (oneList + y + str(x) + "-" +
                           str(blackpieces[i+8]) + ",")
            elif x == 2:
                oneList = (oneList + y + str(x) + "-" +
                           str(whitepieces[i]) + ",")
            elif x == 1:
                oneList = (oneList + y + str(x) + "-" +
                           str(whitepieces[i+8]) + ",")
            else:
                oneList = (oneList + y + str(x) + "-##,")
        oneBoard.append(oneList + "\n")
        oneList = ""
    print(np.matrix(oneBoard))
    file = open(GAMEFILE, "w+")
    file.writelines(oneBoard)


if __name__ == "__main__":
    main()
