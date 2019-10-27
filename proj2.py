# File:    proj2.py
# Author:  Steven Ryan
# Date:    11/3/18
# Section: 34
# E-mail:  sryan6@umbc.edu
# Description:
# A connect four game that plays against a player and a computer

##################################
#### DO NOT TOUCH THESE LINES ####
from random import randint, seed #
seed(100)                        #
##################################

#Miscellaneous Constants
YES = "y"
NO = "n"
UNDERSCORE = "_"
X = "X"
O = "O"

#Board wraparound constant for checking a win
THREE = 3

#Player Constants
ONE = 1
TWO = 2

#Board Size Constants
MIN_HEIGHT = 5
MIN_WIDTH = 5

#Constants for checking a win
WINLIST_X = ["X", "X", "X", "X"]
WINLIST_O = ["O", "O", "O", "O"]

# printBoard(board) prints a connect four board from a list
# 
# Input:    takes in a list to print
# Output:   None, it is a print function
def printBoard(board):
    for i in range(0, len(board)):
        for u in range(0, len(board[i])):
            print(board[i][u], end = " ")
        print("")

# checkWin(board) determines if there is four in a row somewhere in the code.
# 
# Input:    takes in the updated list
# Output:   a boolean, True if a win condition is met and False if not.
def checkWin(board):
    
    #Checks horizontal win condition
    for i in range(0, len(board)):
        for u in range(0, len(board[i])-THREE):
            compareList = []
            compareList.append(board[i][u])
            compareList.append(board[i][u+1])
            compareList.append(board[i][u+2])
            compareList.append(board[i][u+3])
            if(compareList == WINLIST_X):
                return True
            if(compareList == WINLIST_O):
                return True

    #Checks vertical win condition
    for i in range(0, len(board)-THREE):
        for u in range(0, len(board[i])):
            compareList = []
            compareList.append(board[i][u])
            compareList.append(board[i+1][u])
            compareList.append(board[i+2][u])
            compareList.append(board[i+3][u])
            if(compareList == WINLIST_X):
                return True
            if(compareList == WINLIST_O):
                return True

    #Checks decreasing diagonal win condition
    for i in range(0, len(board)-THREE):
        for u in range(0, len(board[i])-THREE):
            compareList = []
            compareList.append(board[i][u])
            compareList.append(board[i+1][u+1])
            compareList.append(board[i+2][u+2])
            compareList.append(board[i+3][u+3])
            if(compareList == WINLIST_X):
                return True
            if(compareList == WINLIST_O):
                return True

    #Checks increasing diagonal win condition
    for i in range(0, len(board)-THREE):
        for u in range(THREE, len(board[i])):
            compareList = []
            compareList.append(board[i][u])
            compareList.append(board[i+1][u-1])
            compareList.append(board[i+2][u-2])
            compareList.append(board[i+3][u-3])
            if(compareList == WINLIST_X):
                return True
            if(compareList == WINLIST_O):
                return True
    
    return False

# placeDisk(board, player, choice) if the player is 1, the corresponding _ in
#           the list is replaced with an x and an o for player 2. Puts the
#           choice at the bottom-most open spot
# 
# Input:    the list that represents the board, the choice column to replace
#           the _ in the list, and the player to tell what to replace the _
#           with.
# Output:   returns the updated list of values
def placeDisk(board, player, choice):
    choice -= 1
    exitFlag = False
    CountdownIndex = len(board) - 1
    if(player == ONE):
        while(CountdownIndex >= 0 and exitFlag == False):
            if(board[CountdownIndex][choice] == UNDERSCORE):
                board[CountdownIndex][choice] = X
                exitFlag = True
            else:
                CountdownIndex -= 1
    elif(player == TWO):
        while(CountdownIndex >= 0 and exitFlag == False):
            if(board[CountdownIndex][choice] == UNDERSCORE):
                board[CountdownIndex][choice] = O
                exitFlag = True
            else:
                CountdownIndex -= 1
    return board

# main
def main():
    playAgain = YES
    
    while(playAgain == YES):
        player = TWO
        winFlag = False
        TieFlag = False
        pieceCounter = 0
        board = []

        # Asks user for a height of the board
        height = int(input("Enter a height: "))
        while(height < MIN_HEIGHT):
            height = int(input("You must give a number higher than 4: "))
        # Asks user for a width of the board
        width = int(input("Enter a width: "))
        while(width < MIN_WIDTH):
            width = int(input("You must give a number higher than 4: "))
        # tallies up the number of spaces filled in order to get a tie
        tieNumber = height * width

        #Creates the board
        for i in range(0, height):
            boardRow = []
            for u in range(0, width):
                boardRow.append(UNDERSCORE)
            board.append(boardRow)
                
        mode = input("Play against the computer? (y/n): ")
        while(mode != YES and mode != NO):
              mode = input("please enter a 'y' or a 'n': ")

        #Starts 1 player mode
        if(mode == YES):
            while(winFlag == False and TieFlag == False):
                # switches the player
                if(player == ONE):
                    player = TWO
                elif(player == TWO):
                    player = ONE
                # prints board
                printBoard(board)
                #player 1's turn
                if(player == ONE):
                    print("Enter a column (1-", width, end = "")
                    choice = int(input("): "))

                    #checks if the input is a valid column within the range
                    while(choice < ONE or choice > width):
                        print("Enter a valid column (1-", width, end = "")
                        choice = int(input("): "))

                    #checks to see if the column is full
                    while(board[0][choice - 1] != UNDERSCORE):
                        print("That column is full! ", end = "")
                        print("Choose again (1-", width, end = "")
                        choice = int(input("): "))

                    #updates the board with the column placed
                    board = placeDisk(board, player, choice)
                    pieceCounter += 1

                    #checks to see if a win or tie condition has been met
                    winFlag = checkWin(board)
                    if(pieceCounter >= tieNumber and winFlag == False):
                        TieFlag = True
                #Computer's turn
                elif(player == TWO):
                    print("Computer's Move:")
                    choice = randint(ONE, width)

                    #checks to see if the column is full
                    while(board[0][choice - 1] != UNDERSCORE):
                        choice = randint(ONE, width)
                    
                    print("Computer chose column", choice)
                    #updates the board with the column placed
                    board = placeDisk(board, player, choice)
                    pieceCounter += 1
                    
                    #checks to see if a win or tie condition has been met
                    winFlag = checkWin(board)
                    if(pieceCounter >= tieNumber and winFlag == False):
                        TieFlag = True

            #displays who wins
            if(winFlag != False):
                if(player == ONE):
                    print("\nplayer", player, "wins!!!\n")
                elif(player == TWO):
                    print("\nComputer wins!!!\n")
            elif(TieFlag != False):
                print("It was a Tie!")

        #Starts 2 player mode
        elif(mode == NO):
            while(winFlag == False and TieFlag == False):
                #switches player
                if(player == ONE):
                    player = TWO
                elif(player == TWO):
                    player = ONE
                #prints board
                printBoard(board)
                print("Player", player, end = "")
                print("'s move")
                print("Enter a column (1-", width, end = "")
                choice = int(input("): "))

                #checks if the input is a valid column within the range
                while(choice < ONE or choice > width):
                    print("Enter a valid column (1-", width, end = "")
                    choice = int(input("): "))

                #checks to see if the column is full
                while(board[0][choice - 1] != UNDERSCORE):
                    print("That column is full! ", end = "")
                    print("Choose again (1-", width, end = "")
                    choice = int(input("): "))
                    
                #updates the board with the column placed
                placeDisk(board, player, choice)
                pieceCounter += 1
                    
                #checks to see if a win or tie condition has been met
                winFlag = checkWin(board)
                if(pieceCounter >= tieNumber and winFlag == False):
                        TieFlag = True

            #states who wins            
            if(winFlag != False):
                print("\nplayer", player, "wins!!!\n")
            elif(TieFlag != False):
                print("It was a tie!")

        #asks if the player wants to play again
        print("Ending Gameboard:")
        printBoard(board)
        playAgain = input("play again? (y/n): ")
        while(playAgain != YES and playAgain != NO):
              playAgain = input("please enter a 'y' or a 'n': ")
main()
