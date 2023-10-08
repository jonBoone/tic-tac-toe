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


if __name__ == "__main__":
    print("hello tic-tac-toe!\n", end="")
