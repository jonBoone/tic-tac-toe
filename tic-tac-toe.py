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
        assert self.grid[row][col] is None, "someone already claimed this spot"
        theRow = self.grid[row]
        theRow[col] = marker

    def takeTurn(self, playerMarker):
        """gather input from the player and add it to the board """
        row = -1
        col = -1
        while not(self.validate(row) and self.validate(col)):
            row, col = [int(a) for a in
                        input(f"Enter the row and col for {playerMarker}'s turn: ").split()]
            if self.validate(row) and self.validate(col):
                self.set(row, col, playerMarker)
                break

    def validate(self, index):
        """
        validate the index is in range
        """
        return index >= 0 and index < self.gridSize


if __name__ == "__main__":
    print("hello tic-tac-toe!\n", end="")
