#!/usr/bin/env python

#
# tic-tac-toe.py
#
# Author: Jon Boone <ipmonger@delamancha.org>
#

class Board:
    """ Tic-Tac-Toe Board"""

    def __init__(self, player1, player2):
        """ defines the instance data members"""
        self.gridSize = 3
        self.grid = [[None for _ in range(self.gridSize)] for _ in range(self.gridSize)]
        self.players = [player1, player2]
        self.winDescriptions = { 0: "Top Row", 1: "Middle Row",
                                 2: "Bottom Row", 3: "Left Column",
                                 4: "Middle Column", 5: "Right Column",
                                 6: "Diagonal (Top Left to Bottom Right",
                                 7: "Diagonal (Bottom Left to Upper Right)"
                                }

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

    def _compareLists_(self, win, possibleWin):
        return win == possibleWin


    def _generatePotentialWins_(self):
        potentials = []
        #rows
        [potentials.append([self.grid[row][col] for col in range(self.gridSize)])
         for row in range(self.gridSize)]
        #cols
        [potentials.append([self.grid[row][col] for row in range(self.gridSize)])
         for col in range(self.gridSize)]
        #diagLtoR
        potentials.append([self.grid[0][0], self.grid[1][1], self.grid[2][2]])
        #diagRtoL
        potentials.append([self.grid[0][2], self.grid[1][1], self.grid[2][0]])

        return potentials


    def _setRowCol_(self, row: int, col: int, player: Marker):
        """put the player's symbol in the spot unless its already been taken """
        if not self.grid[row][col] is None:
            raise ValueError(f"{player}'s selected spot {row} {col} is already taken")
        self.grid[row][col] = str(player)


    def _validate_(self, index):
        """
        validate the index is in range
        """
        if not (index >= 0 and index < self.gridSize):
            raise ValueError(f"{index} is not between 0 and {self.gridSize - 1}")

        return index >= 0 and index < self.gridSize


    def checkWin(self, player):
        """check the board to see if anyone has won """
        win = [f"{player}", f"{player}", f"{player}"]

        potentialWins = self._generatePotentialWins_()

        for testCase in range(len(potentialWins)):
            if self._compareLists_(win, potentialWins[testCase]):
                return (True, self.winDescriptions[testCase])

        return (False, None)


    def recordTurn(self, player):
        """gather input from the player and add it to the board """
        row = -1
        col = -1
        while True:
            row, col = [int(a) for a in
                        input(f"Enter the row and col for {player}'s turn: ").split()]
            try:
                self._validate_(row)
                self._validate_(col)
                self._setRowCol_(row, col, player)
                break
            except ValueError as ve:
                print(f"{ve.args}, try again")


class Marker:
    """The marker for a particular player """

    def __init__(self, symbol: str):
        self.symbol = symbol

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.symbol)


class Game:
    """An instance of this class represents a single game of Tic-Tac-Toe """

    def __init__(self,board: Board, index=0):
        self.board = board
        self.players = board.players
        self.index = index






def main():
    player1 = Marker("X")
    player2 = Marker("O")
    board = Board(player1, player2)

    board.recordTurn(player1)
    print(board)
    won, typeOfWin = board.checkWin(player1)
    if won:
        print(f"{player1} wins {typeOfWin}!!!!!")

    board.recordTurn(player2)
    print(board)
    won, typeOfWin = board.checkWin(player2)
    if won:
        print(f"{player2} wins {typeOfWin}!!!!!!")


if __name__ == "__main__":
    main()
    player1 = Marker("λ")
    player2 = Marker("𝞴")
    myBoard = Board(player1, player2)
