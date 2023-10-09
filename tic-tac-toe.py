#!/usr/bin/env python

#
# tic-tac-toe.py
#
# Author: Jon Boone <ipmonger@delamancha.org>
#

import re

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

    def __init__(self, player1, player2):
        """ defines the instance data members"""
        self.gridSize = 3
        self.grid = [[None for _ in range(self.gridSize)] for _ in range(self.gridSize)]
        self.players = [player1, player2]
        self.winDescriptions = { 0: "top row", 1: "middle row",
                                 2: "bottom row", 3: "left column",
                                 4: "middle column", 5: "right column",
                                 6: "diagonal (top left to bottom right",
                                 7: "diagonal (bottom left to upper right)"
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
                        input(f"Enter the row (0-2) and col (0-2) for {player}'s turn: ").split()]
            try:
                self._validate_(row)
                self._validate_(col)
                self._setRowCol_(row, col, player)
                break
            except ValueError as ve:
                print(f"{ve.args}, try again")


class Game:
    """An instance of this class represents a single game of Tic-Tac-Toe """

    def __init__(self, player1, player2, gameNumber=0):
        self.board = Board(player1, player2)
        self.gameNumber = gameNumber
        self.players = [player1, player2]
        self.maxTurns = 9
        self.nextTurn = 0

    def _reportDraw(self):
        print(f"It's a draw - neither {self.players[0]} nor {self.players[1]} wins!")

    def _reportWin(self, player, winType):
        print(f"{player} wins along the {winType}!!!!!")


    def _takeTurn(self):
        player = self.players[self.nextTurn % 2]
        self.board.recordTurn(player)
        print(f"\n{self.board}\n")
        self.nextTurn += 1
        return (self.board.checkWin(player), player)

    def _welcome_(self):
        print(f"Starting a new game {self.players[0]} v {self.players[1]}: ",end="")
        print(f"{self.players[0]} goes first!\n")

    def alternateTurns(self):
        won = False
        while self.nextTurn < self.maxTurns:
            (won, winType), player = self._takeTurn()
            if won:
                self._reportWin(player, winType)
                break
        if not (won):
            self._reportDraw()
        print("\n\n")

    def begin(self):
        self._welcome_()
        print(f"{self.board}\n")


def confirm():
    response = False
    confirmRE = re.compile("^([yY]|[yY][eE][sS])$")
    another = input(f"Would you like to play again? ")
    if confirmRE.match(another) is not None:
        response = True
    return response

def goodbye():
    print("Thanks for playing!")



def main():
    player1 = Marker("X")
    player2 = Marker("O")
    gameNum = 0
    another = True

    while another:
        game = Game(player1, player2, gameNum)
        game.begin()
        game.alternateTurns()
        another = confirm()
        if another:
            gameNum += 1

    goodbye()


if __name__ == "__main__":
    main()
    player1 = Marker("λ")
    player2 = Marker("𝞴")
    myBoard = Board(player1, player2)
