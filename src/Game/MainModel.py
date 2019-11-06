import pygame
import random


blocks = [

    [[1, 1, 1],

     [0, 1, 0]],


    [[0, 2, 2],

     [2, 2, 0]],


    [[3, 3, 0],

     [0, 3, 3]],


    [[4, 0, 0],

     [4, 4, 4]],


    [[0, 0, 5],

     [5, 5, 5]],


    [[6, 6, 6, 6]],


    [[7, 7],

     [7, 7]]

]


class MainModel:
    def __init__(self, width, height):

        self.width = 10
        self.height = 20
        self.curr_x_pos = 4 #The middle right of the block
        self.curr_y_pos = 1 #The bottom of the block
        self.level = 1
        self.score = 0
        self.curr_block = random.choice(blocks)
        self.curr_block_h = len(self.curr_block)
        self.curr_block_w = len(self.curr_block[0])
        self.curr_block_lowest = self.get_block_lowest()

        self.grid = []

    def make_grid(self):
        '''
        (DoomFall) -> None
        Given width, height as 10 and 20 respectively,
         create a 2D grid
           '''

        for i in range(self.height):
            self.grid.append([])
            for j in range(self.width):
                self.grid[i].append('[ ]')

        self.grid[self.curr_x_pos][self.curr_y_pos] = random.choice(blocks)

    def move_block_left(self) -> None:
        """
        Move the current block 1 grid to the left
        if it is out of bound, ignore it
        """
        if self.curr_x_pos > self.curr_block_w/2:
            self.curr_x_pos -= 1

    def move_block_right(self) -> None:
        """
        Move the current block 1 grid to the right
        if it is out of bound, ignore it
        """
        if self.curr_x_pos + (self.curr_block_w-1)/2 < self.width:
            self.curr_x_pos += 1

    def get_level(self):
        return self.level

    def get_score(self):
        return self.score

    def get_block_lowest(self) -> list:
        """
        get a list of relative position of each column from the lowest point of
        the block to the lowest point of that column
        :return:
        """
        lst = [0] * self.curr_block_w
        for x in range(self.curr_block_w):
            y = self.curr_block_h
            while self.curr_block[y][x] != 0:
                lst[x] += 1
                y -= 1
        return lst


