import pygame

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
        self.curr_x_pos = 4
        self.curr_y_pos = 1
