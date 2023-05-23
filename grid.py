
#imports
import numpy as np
import random
from dictionary import colors
"""
A .py class that stores the Board object class.
Contains an initialization, some debugging definitions, and
handles board movement and new piece generation.

"""
class Board:

    #initialization of instance
    def __init__(self, size):
        """
        self.score: stores the score of the current instance of the game
        self.full: a boolean value that returns if the board is full
        self.grid: the 4x4 np array that will store the values of the tiles
        throughout tile movements and new piece generation.

        """
        self.score = 0
        self.full = False
        self.grid = np.zeros((4, 4), dtype = int)
    
    #for debugging
    def __str__(self):
        return str(self.grid)
    
    def take_turn(self, direc):
        """
        calls _move to handle the movements of the board
        returns board once this is done
        """
        self.grid = self._move(direc)
        return self.grid
    
    def getBoard(self):
        """
        Returns the board
        """
        regBoard = [[0 for _ in range(4)] for _ in range(4)]

        for i in range(4):
            for j in range(4):
                regBoard[i][j] = self.grid[i][j]
        return regBoard
 
    def _move(self, direc):
        """
        Description: Assumes the game is still playing.  Shifts the board
        accordingly, and controls the majority of the actual movement that
        occurs in this board.

        For every direction:
            1. shift the tiles up, down, left, or right, respectively
            2. merge values when needed and valid

        Inputs: the direction that the key pressed indicated, represented as
        a string of UP, DOWN, LEFT, RIGHT.

        The board that will be updated from that direction.

        Returns: the updated board, with tiles in updated positions from
        the direction indicated.

        """
        merged = np.zeros((4, 4), dtype=bool)
        if direc == 'UP':
            for j in range(4):
                for i in range(1, 4):
                    shift = 0
                    if self.grid[i][j] != 0:
                        for q in range(i):
                            if self.grid[q][j] == 0:
                                shift += 1
                        if shift > 0:
                            self.grid[i - shift][j] = self.grid[i][j]
                            self.grid[i][j] = 0
                        if i - shift - 1 >= 0:
                            if self.grid[i - shift - 1][j] == self.grid[i - shift][j] and not merged[i - shift][j] \
                                    and not merged[i - shift - 1][j]:
                                self.grid[i - shift - 1][j] *= 2
                                self.score += self.grid[i - shift - 1][j]
                                self.grid[i - shift][j] = 0
                                merged[i - shift - 1][j] = True
        elif direc == 'LEFT':
            for i in range(4):
                for j in range(1, 4):
                    shift = 0
                    if self.grid[i][j] != 0:
                        for q in range(j):
                            if self.grid[i][q] == 0:
                                shift += 1
                        if shift > 0:
                            self.grid[i][j - shift] = self.grid[i][j]
                            self.grid[i][j] = 0
                        if j - shift - 1 >= 0:
                            if self.grid[i][j - shift - 1] == self.grid[i][j - shift] and not merged[i][j - shift - 1] \
                                    and not merged[i][j - shift]:
                                self.grid[i][j - shift - 1] *= 2
                                self.score += self.grid[i][j - shift - 1]
                                self.grid[i][j - shift] = 0
                                merged[i][j - shift - 1] = True

        elif direc == 'RIGHT':
            for i in range(4):
                for j in range(4):
                    shift = 0
                    if self.grid[i][3-j] != 0:
                        for q in range(j):
                            if self.grid[i][3-q] == 0:
                                shift += 1
                        if shift > 0:
                            self.grid[i][3-j+shift] = self.grid[i][3-j]
                            self.grid[i][3-j] = 0
                        if 3-j+shift-1 >= 0:
                            if self.grid[i][3-j+shift-1] == self.grid[i][3-j+shift] and not merged[i][3-j+shift-1] \
                                and not merged[i][3-j+shift]:
                                self.grid[i][3-j+shift-1] *= 2
                                self.score += self.grid[i][3-j+shift-1]
                                self.grid[i][3-j+shift] = 0
                                merged[i][3-j+shift-1] = True
        
        elif direc == 'DOWN':
            for j in range(4):
                for i in range(2, -1, -1):
                    shift = 0
                    if self.grid[i][j] != 0:
                        for q in range(i, 4):
                            if self.grid[q][j] == 0:
                                shift += 1
                        if shift > 0:
                            self.grid[i + shift][j] = self.grid[i][j]
                            self.grid[i][j] = 0
                        if i + shift + 1 <= 3:
                            if self.grid[i + shift + 1][j] == self.grid[i + shift][j] and not merged[i + shift][j] \
                                    and not merged[i + shift + 1][j]:
                                self.grid[i + shift + 1][j] *= 2
                                self.score += self.grid[i + shift + 1][j]
                                self.grid[i + shift][j] = 0
                                merged[i + shift + 1][j] = True
        return self.grid

    def new_pieces(self):
        """
        Description: creates a new, randomized board value in an 'open', 
        zero spot anywhere in the board.  Important for the initalization,
        where we put 2 values of 2 and/or 4 in any board.  Also important
        for every turn that we 

        Inputs: the board, which needs a new piece

        Returns: the updated board and a boolean denoting

        """
        #count value to be updated throughout loop
        count = 0
        #randomly creates a value of 2 or 4 in an open place
        while any(0 in row for row in self.grid) and count < 1:

            #randomly generate rows and colums
            row = random.randint(0, 3)
            col = random.randint(0, 3)

            #if we find an empty tile, randomly generate!
            if self.grid[row][col] == 0:
                count += 1
                if random.randint(1, 10) == 10:
                    self.grid[row][col] = 4
                else:
                    self.grid[row][col] = 2
        # lets us know if the board is full and we don't need to introduce a value
        if count < 1:
            self.full = True
        
        #return the if the board is full 
        return self.grid, self.full
    

