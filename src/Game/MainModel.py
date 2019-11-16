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
    def __init__(self):

        self.width = 10
        self.height = 24

        # The middle of the block, middle right if the block has even width
        self.curr_x_pos = 2
        self.curr_y_pos = 2  # The bottom of the block

        self.level = 1
        self.score = 0

        self.curr_block = random.choice(blocks)
        self.curr_block_h = len(self.curr_block[0])
        self.curr_block_w = len(self.curr_block)
        self.curr_block_lowest = self._get_block_lowest()
        # The leftmost position of the block
        #self.curr_block_left = self.curr_x_pos - self.curr_block_w//2
        # The rightmost position of the block
        #self.curr_block_right = self.curr_x_pos + (self.curr_block_w+1)//2

        self.next_block = random.choice(blocks)

        self.grid = []

    def get_leftmost(self) -> int:
        return self.curr_x_pos - self.curr_block_w//2

    def get_rightmost(self) -> int:
        return self.curr_x_pos + (self.curr_block_w + 1) // 2

    def get_botmost(self) -> int:
        return self.curr_y_pos + (self.curr_block_h+1)//2

    def make_grid(self):
        '''
        (DoomFall) -> None
        Given width, height as 10 and 24 respectively,
         create a 2D grid
           '''

        for i in range(self.height):
            self.grid.append([])
            for j in range(self.width):
                self.grid[i].append('[0]')

        self.grid[self.curr_x_pos][self.curr_y_pos] = random.choice(blocks)

    def move_block_left(self) -> None:
        """
        Move the current block 1 grid to the left
        if it is out of bound, ignore it
        """
        if self.get_leftmost() > 0:
            self.curr_x_pos -= 1

    def move_block_right(self) -> None:
        """
        Move the current block 1 grid to the right
        if it is out of bound, ignore it
        """
        if self.get_rightmost() < self.width:
            self.curr_x_pos += 1

    def get_level(self):
        return self.level

    def get_score(self):
        return self.score

    def _get_block_lowest(self) -> list:
        """
        get a list of relative position of each column from the lowest point of
        the block to the lowest point of that column
        :return:
        """
        lst = [0] * self.curr_block_w
        for x in range(self.curr_block_w):
            y = 0
            while self.curr_block[x][y] == 0:
                lst[x] += 1
                y += 1
        return lst

    def _collision(self) -> bool:
        """
        determine if the block collide with the floor or another block
        :return: True if there is a collide
        """
        bot = 0
        for x in range(self.get_leftmost(), self.get_rightmost()):
            if self.get_botmost() == 23:
                return True
        return False

    def get_next_block(self) -> list:
        """
        :return: next dropping block
        """
        return self.next_block

    def get_delay(self) -> int:
        return max(750//self.level, 17)

    def drop_block(self) -> None:
        """
        drop the block to bottom
        :return:
        """
        while not self._collision():
            self.curr_y_pos += 1

