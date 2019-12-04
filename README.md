# DOOMFALL

Tetris insipired game created in `Python` with the help of `pygame`


# Navigation
- [Game Description](https://github.com/ArturAzarskyy/DOOMFALL#Game-Description)
  - [Controls](https://github.com/ArturAzarskyy/DOOMFALL#Controls)
  - [Screenshots](https://github.com/ArturAzarskyy/DOOMFALL#Screenshots)
- [Installation](https://github.com/ArturAzarskyy/DOOMFALL#Installation)
- [Documentation](https://github.com/ArturAzarskyy/DOOMFALL#Documentation)
- [Authors](https://github.com/ArturAzarskyy/DOOMFALL#Authors)
- [License](https://github.com/ArturAzarskyy/DOOMFALL#License)

# Game Description

Doomfall is a simple implementation of tetris in `Python` using `pygame`

The goal of DOOMFALL is to strategically place falling blocks in a way to create horizontal row(s) on the screen. When one or more rows is formed, the row disappears, increasing your score and dropping the already placed blocks slightly farther down. As you play the game your score will be increased with each block placed, and every horizontal row cleared. Once you have no more space to place a new block the game is over.

# Controls
The controls for DOOMFALL are quite simple:

- A&D or left&right arrow keys to move left and right respectively
- Q&E to rotate counter-clockwise or clockwise respectively
- SPACE to drop the block all the way down.

# Screenshots
![screenshot](https://i.imgur.com/lzZci0g.png)


# Installation

# Documentation
- #### MainView:
   - `draw_block(self, pygame_window, old_pos, game)`
- #### MainModel:
  Main model saves all of the blocks in `self.grid`, models is also responsible for attempting to move and rotate the blocks as well as keeping the track of the score and level of the game. If model has ability to rotate or move the block it will request [MainView](https://github.com/ArturAzarskyy/DOOMFALL#MainView) to redraw the block.
  - move_block_left(self):
     - Attempts the movement of the block to the left, if it can be successfully moved the function then decreases the `self.curr_x_pos` by 1.
   - move_block_right(self):
      - Attempts the movement of the block to the right, if it can be successfully moved the function then increases the `self.curr_x_pos` by 1.
   - request_draw(self):
      - If block did't reach the bottom of the grid it will request  [MainView](https://github.com/ArturAzarskyy/DOOMFALL#MainView) to redraw the block.
	 - If block at the bottom of the grid [MainModel](https://github.com/ArturAzarskyy/DOOMFALL#MainModel) `self.is_at_the_bottom()`


- #### MainController:
  MainController is responsible for requesting specific actions from the [MainModel](https://github.com/ArturAzarskyy/DOOMFALL#MainModel)
   - read_event(self, `event`):
     - `event`: pygame `event` which was ditected(Ex. mose button pressed, 'A' pressed)
   - \_rotate(self, `direction`):
     - Promts MainModel to rotate block clockwise or counter-clockwise.
   - direction: -1 to prompt rotation in counter-clockwise direction of the block, 1  to prompt rotation in clockwise direction of the block
   - \_move(self, `direction`):
     - Prompts MainModel to move block to the left or right.
     - `direction`: -1 to prompt movement of the block to the left, 1 to prompt movement of the block to the right
   - \_drop_block(self):
     - Requests MainModel to move block to the bottomost postition.

# Authors
 - Daniel Apushkinsky
 - Artur Azarskyy
 - Abdul Aleem
 - Chi Fung Chan

# License
This project is licensed under the GNU GENERAL PUBLIC LICENSE License - see the [LICENSE.md](LICENSE.md) file for details

[Back to top](https://github.com/ArturAzarskyy/DOOMFALL#DOOMFALL)
