import string

TEXT = "game.txt"
alphabetsoup = list(map(chr, range(97, 105)))
print(alphabetsoup)


def main():
    oneList = ""
    oneBoard = []

    for x in range(8, 0, -1):
        for y in alphabetsoup:
            oneList = (oneList + "("+y+str(x)+"-)")
        oneBoard.append(oneList + "\n")
        oneList = ""
    print(oneBoard)

    file = open(TEXT, "w+")
    file.writelines(oneBoard)


if __name__ == "__main__":
    main()
