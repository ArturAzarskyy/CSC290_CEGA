import pygame
import random
from copy import deepcopy

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
    def __init__(self, view):

        self.width = 10
        self.height = 20
        self.view = view

        # The middle of the block, middle right if the block has even width
        self.curr_x_pos = 5
        self.curr_y_pos = 0  # The bottom of the block

        self.level = 1
        self.score = 0
        self.is_game_over = False

        self.curr_block = random.choice(blocks)
        self.curr_block_h = len(self.curr_block)
        self.curr_block_w = len(self.curr_block[0])
        self.next_block = random.choice(blocks)

        self.grid = []
        self.make_grid()

    def get_leftmost(self) -> int:
        return self.curr_x_pos #- self.curr_block_w//2

    def get_rightmost(self) -> int:
        if self.curr_block == blocks[-1]:
            return self.curr_x_pos + (self.curr_block_w +2) // 2
        return self.curr_x_pos + (self.curr_block_w +4) // 2

    def get_botmost(self) -> int:
        if self.curr_block == blocks[-2]:
            return self.curr_y_pos + 1
        return self.curr_y_pos #+ (self.curr_block_h+1)//2

    def make_grid(self):
        '''
        (DoomFall) -> None
        Given width, height as 10 and 24 respectively,
         create a 2D grid
           '''

        for i in range(self.height):
            self.grid.append([])
            for j in range(self.width):
                self.grid[i].append(0)

        #self.grid[self.curr_x_pos][self.curr_y_pos] = random.choice(blocks)

    def request_draw(self):
        if self.curr_y_pos < self.height:
            self.view.previous_position = self.view.draw_block(self.view.win, self.view.previous_position, self)
        else:
            self.is_at_the_bottom()

    def can_spawn_block(self) -> bool:
        """
        Returns if the game is still playable, or if it should be ended
        """
        #print(self.row[0])
        for i in range(0, 2):
            for j in range(4, 8):
                if self.grid[i][j] != 0:
                    return False
        return True

    def get_full_lines(self) -> list:
        """
        Returns a list of row in which there is a full line
        """
        ans = []
        for row in range(len(self.grid)):
            row_full = True
            for square in self.grid[row]:
                if square == 0:
                    row_full = False
                    break
            if row_full:
                ans.append(row)
        return ans

    def is_at_the_bottom(self):
        if self.curr_y_pos == self.height -2 :
            #self.reset_block()
            return True
        return False

    def reset_block(self):
        self.curr_block = self.next_block
        self.next_block = random.choice(blocks)
        self.curr_x_pos = 5 - len(self.curr_block[0])//2
        self.curr_y_pos = -1

    def can_move_down(self):
        if self.is_at_the_bottom():
            return False

        for i in range(len(self.curr_block)):
            for j in range(len(self.curr_block[0])):
                if self.curr_block[i][j] != 0:
                    if self.get_botmost()+1+i >= len(self.grid) or self.grid[self.get_botmost()+1+i][self.get_leftmost()+j] != 0:
                        #self.reset_block()
                        return False
        return True

    def can_move_left(self):
        if not self.get_leftmost() > 0:
            return False

        for i in range(len(self.curr_block)):
            for j in range(len(self.curr_block[0])):
                if self.curr_block[i][j] != 0:
                    if self.grid[self.get_botmost()+i][self.get_leftmost()+j-1]\
                            != 0:
                        return False
        return True

    def can_move_right(self):
        if not self.get_rightmost() < self.width:
            return False

        for i in range(len(self.curr_block)):
            for j in range(len(self.curr_block[0])):
                if self.curr_block[i][j] != 0:
                    if self.grid[self.get_botmost()+i][self.get_leftmost()+j+1]\
                            != 0:
                        return False
        return True

    def move_block_left(self) -> None:
        """
        Move the current block 1 grid to the left
        if it is out of bound, ignore it
        """
        if self.can_move_left():
            self.curr_x_pos -= 1
            self.request_draw()

    def move_block_right(self) -> None:
        """
        Move the current block 1 grid to the right
        if it is out of bound, ignore it
        """
        if self.can_move_right():
            self.curr_x_pos += 1
            self.request_draw()

    def place_block_in_grid(self, info) -> None:
        """
        Info is a tuple of the x pos, y pos and block.
        This method places the given block at the (x,y) position on the grid
        """
        for i in range(len(info[2])):
            for j in range(len(info[2][0])):
                if info[2][i][j] != 0:
                    self.grid[info[1]+i][info[0]+j] = info[2][i][j]

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
        lst = [0] * self.curr_block_h
        for x in range(self.curr_block_h):
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
        while self.can_move_down():
            self.curr_y_pos += 1

    def rotate_right(self):
        h = len(self.curr_block)
        w = len(self.curr_block[0])

        temp = [0] * h
        ans = [temp] * w

        for i in range(len(self.curr_block[0])):
            temp_row = [0] * h

            for j in range(len(self.curr_block)):
                temp_row[j] = self.curr_block[j][i]
            ans[i] = temp_row[::-1]

        self.curr_y_pos += len(ans) - self.curr_block_h
        self.curr_x_pos += len(ans[0]) - self.curr_block_w # not sure about this line
        self.curr_block_w = len(ans[0])
        self.curr_block_h = len(ans)
        self.curr_block = deepcopy(ans)
