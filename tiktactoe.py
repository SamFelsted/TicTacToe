gameBoard = {
    1:"1", 2:"2", 3:"3",
    4:"4", 5:"5", 6:"6",
    7:"7", 8:"8", 9:"9" 
}
playerOneTurn = 1
def winCheck():
    for x in range(1, 3):
        if gameBoard[x] == gameBoard[x + 1] == gameBoard[x + 2]:
            return True
        elif gameBoard[x] == gameBoard[x + 3] == gameBoard[x + 6]:
            return True
        elif gameBoard[1] == gameBoard[5] == gameBoard[9]:
            return True
        elif gameBoard[3] == gameBoard[5] == gameBoard[7]:
            return True

def draw():
    print(gameBoard[1]+ "|" + gameBoard[2] + "|" + gameBoard[3]) 
    print(gameBoard[4]+ "|" + gameBoard[5] + "|" + gameBoard[6])
    print(gameBoard[7]+ "|" + gameBoard[8] + "|" + gameBoard[9])

def main():
    global playerOneTurn
    draw()
    if playerOneTurn < 10:
        if playerOneTurn % 2 == 1:
            space = input("Player one, where would you like to go? ")
            if gameBoard[space] == str(space):
                gameBoard[space] = "X"
                playerOneTurn += 1
                if winCheck():
                    print("Player one has won")
                    draw()
                else:
                    main()
            else:
                print("Square not valid try again you fool")
                main()
        else:
            space = input("Player two, where would you like to go? ")
            if gameBoard[space] == str(space):
                gameBoard[space] = "O"
                playerOneTurn += 1
                if winCheck():
                    print("Player two has won")
                    draw()
                else:
                    main()
            else:
                print("Square not valid try again you fool")
                main()
    else:
        print("Tie")

main()