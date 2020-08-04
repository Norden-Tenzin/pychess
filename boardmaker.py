import string

TEXT = "game.txt"

alphabetsoup = list(map(chr, range(97, 105)))
print(alphabetsoup)


def listRev():
    oneList = ""
    oneBoard = []

    for x in range(8, 0, -1):
        for y in alphabetsoup:
            oneList = (oneList + "("+y+str(x)+"-)")
        oneBoard.append(oneList + "\n")
        oneList = ""
    print(oneBoard)
    return oneBoard


def main():
    output = listRev()

    file = open(TEXT, "w+")
    file.writelines(output)


if __name__ == "__main__":
    main()
