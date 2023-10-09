#!/usr/bin/env python

#
# tic-tac-toe.py
#
# Author: Jon Boone <ipmonger@delamancha.org>
#


class Marker:
    """The marker for a particular player """

    def __init__(self, symbol: str):
        self.symbol = symbol

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.symbol)


class Board:
    """ Tic-Tac-Toe Board"""

    def __init__(self):
        """ defines the instance data members"""
        self.gridSize = 3
        self.grid = [[None for _ in range(self.gridSize)] for _ in range(self.gridSize)]

    def __str__(self):
        """Ensure we print out the grid contents as desired"""
        outStr = ""
        for row in range(self.gridSize):
            for col in range(self.gridSize):
                if self.grid[row][col] is None:
                    outStr += " "
                else:
                    outStr += str(self.grid[row][col])
                if col < self.gridSize - 1:
                    outStr += "|"
            if row < self.gridSize - 1:
                outStr += '\n'
                outStr += '-----\n'
        return outStr

    def checkWin(self, marker):
        """check the board to see if anyone has won """
        win = [f"{marker}", f"{marker}", f"{marker}"]

        possibleWins = self.generatePossibleWins(marker)

        for testCase in range(len(possibleWins)):
            print(f"comparing {win} to {possibleWins[testCase]} \
            (posibleWins{testCase})")

            if self.compare(win, possibleWins[testCase]):
                return (True, testCase)

        return (False, None)

    def compare(self, win, possibleWin):
        return win == possibleWin


    def generatePossibleWins(self, marker):
        possibleWins = []
        #rows
        [possibleWins.append([self.grid[row][col] for col in range(self.gridSize)])
                             for row in range(self.gridSize)]
        #cols
        [possibleWins.append([self.grid[row][col] for row in range(self.gridSize)])
                             for col in range(self.gridSize)]
        #diagLtoR
        possibleWins.append([self.grid[0][0], self.grid[1][1], self.grid[2][2]])
        #diagRtoL
        possibleWins.append([self.grid[0][2], self.grid[1][1], self.grid[2][0]])
        return possibleWins

    def recordTurn(self, playerMarker):
        """gather input from the player and add it to the board """
        row = -1
        col = -1
        while True:
            row, col = [int(a) for a in input(f"Enter the row and col for {playerMarker}'s turn: ").split()]
            try:
                self.validate(row)
                self.validate(col)
                self.set(row, col, playerMarker)
                break
            except ValueError as ve:
                print(f"{ve.args}, try again")

    def set(self, row: int, col: int, marker: Marker):
        """put the marker in the spot unless its already been taken """
        if not self.grid[row][col] is None:
            raise ValueError(f"{marker}'s selected spot {row} {col} is already taken")
        self.grid[row][col] = str(marker)

    def validate(self, index):
        """
        validate the index is in range
        """
        if not (index >= 0 and index < self.gridSize):
            raise ValueError(f"{index} is not between 0 and {self.gridSize - 1}")

        return index >= 0 and index < self.gridSize



def main():
    player1 = Marker("X")
    player2 = Marker("O")
    board = Board()

    board.recordTurn(player1)
    print(board)
    if board.checkWin(player1):
        print(f"{player1.symbol} wins!!!!!")

    board.recordTurn(player2)
    print(board)
    if board.checkWin(player2):
        print(f"{player2.symbol} wins!!!!!!")


if __name__ == "__main__":
    main()
    myBoard = Board()
    player1 = Marker("λ")
    player2 = Marker("𝞴")
