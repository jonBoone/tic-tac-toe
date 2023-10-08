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

    def set(self, row: int, col: int, marker: Marker):
        """put the marker in the spot unless its already been taken """
        if not self.grid[row][col] is None:
            raise ValueError(f"{marker}'s selected spot {row} {col} is already taken")
        self.grid[row][col] = marker

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

    board.recordTurn(player2)
    print(board)


if __name__ == "__main__":
    main()
