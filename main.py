def PrintBoard(boardRaw):
    uniBoard = [["\u25a1" for x in range(10)] for y in range(10)]
    lineString = ""
    lineList = []

    # Create board of unicode characters
    for X in range(10):
        for Y in range(10):
            if boardRaw[X][Y] == 1:
                uniBoard[X][Y] = "\u25a0"
    # Format board into list
    for X in range(10):
        lineString += str(X) + " "
        for Y in range(10):
            lineString += uniBoard[X][Y]
            lineString += " "
        lineList.append(lineString)
        lineString = ""
    # Print board
    lineList.reverse()
    for i in lineList:
        print(i)
    print("  0 1 2 3 4 5 6 7 8 9")


board = [[0 for x in range(10)] for y in range(10)]
PrintBoard(board)
running = True

while running:
    x = -1
    y = -1
    # Choose valid coordinates
    while x == -1 and y == -1:
        coordinates = input("What space do you want to take: ")
        x = int(coordinates[-1:])
        y = int(coordinates[:1])
        # (0, 0) == lose
        if x == 0 and y == 0:
            running = False
        # Make sure chosen spot isn't taken
        if board[x][y] == 1:
            print("That space is taken!")
            x = -1
            y = -1
        # Make sure chosen spot is in board range
        if x >= 10 or y >= 10:
            print("That space isn't on the board!")
            x = -1
            y = -1
    # Take spots
    for xMarker in range(10 - x):
        for yMarker in range(10 - y):
            board[xMarker + x][yMarker + y] = 1
    PrintBoard(board)

print("You lost!")
exit()
