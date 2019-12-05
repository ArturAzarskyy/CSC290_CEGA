# DOOMFALL

Tetris insipired game created in `Python` with the help of `pygame`


# Navigation
- [Game Description](https://github.com/ArturAzarskyy/DOOMFALL#Game-Description)
  - [Controls](https://github.com/ArturAzarskyy/DOOMFALL#Controls)
  - [Screenshots](https://github.com/ArturAzarskyy/DOOMFALL#Screenshots)
- [Installation](https://github.com/ArturAzarskyy/DOOMFALL#Installation)
- [Documentation](https://github.com/ArturAzarskyy/DOOMFALL#Documentation)
- [Authors](https://github.com/ArturAzarskyy/DOOMFALL#Authors)
- [Contributions](https://github.com/ArturAzarskyy/DOOMFALL#Contributions)
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
   - draw_block(self, pygame_window, old_pos, game):
     - Draw the current block in the given `pygame_window`
   - draw_text(self,pygame_window, text, x, y):
     - Draw text at the given (x,y) position
   - draw_grid(self, pygame_window):
     - Draw the white vertical and horizantal border lines (`grid`)
   - draw_end_game(self, pygame_window, final_score):
     - Draw a semi-transparent overlay ontop of the last screen, and display the end game information to the player
- #### MainModel:
  Main model saves all of the blocks in `self.grid`, models is also responsible for attempting to move and rotate the blocks as well as keeping the track of the score and level of the game. If model has ability to rotate or move the block it will request [MainView](https://github.com/ArturAzarskyy/DOOMFALL####MainView) to redraw the block.
  - get_leftmost(self):
    - Returns the leftmost x coordinate.

  - get_rightmost(self):
     - Returns the right-most x coordinate.
     
  - get_botmost(self):
    - Returns the y-coord of the bottom of the falling block.
  - can_spawn_block(self):
    - Returns a boolean if a new block has the space to be spawned
  - get_full_lines(self):
    - Return a list of rows in which there is a full line
  - reset_block(self):
    - Reset the current block to its starting position (essentially spawning a new block)
  - move_block_left(self):
     - Attempts the movement of the block to the left, if it can be successfully moved the function then decreases the `self.curr_x_pos` by 1.
   - move_block_right(self):
      - Attempts the movement of the block to the right, if it can be successfully moved the function then increases the `self.curr_x_pos` by 1.
   - request_draw(self):
      - If block did't reach the bottom of the grid it will request  [MainView](https://github.com/ArturAzarskyy/DOOMFALL####MainView) to redraw the block.
	 - If block at the bottom of the grid [MainModel](https://github.com/ArturAzarskyy/DOOMFALL####MainModel) `self.is_at_the_bottom()`
   - place_block_in_grid(self, info):
     - This method places the given block at the (x,y) position on the grid. Info is a tuple of the x pos, y pos and block.
   - drop_block(self):
     - Rotate the current block clockwise, by modifying the 2D-array of `curr_block`


- #### MainController:
  MainController is responsible for requesting specific actions from the [MainModel](https://github.com/ArturAzarskyy/DOOMFALL####MainModel)
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
 
 # Contributions
 - Daniel Apushkinsky:
 	- In this README I had created the DOOMFALL header & short description, part of the navigation, game description, controls, added one screenshot, and added some imformation to Documentation. Throughout the development of the game I have added a multitude of methods: `can_spawn_block()`, `rotate_right()`, `can_rotate_right()`, `get_full_lines()`, `can_move_down()`, `reset_block()`, `place_block_in_grid()`, `draw_block`() (w/ Artur), `draw_end_game()`, `drop_block` controller and `draw_background()`, and made appropriate changes to our `run_game()` method as new methods were created.
 - Artur Azarskyy:
 	- In README I filled out MainCotroller documentation as well as documentaion for `move_block_left`, `move_block_right`, `request_draw`. I also generated licence and added licence fields into the file, as well as auhtors. In the codebase I created general archetecture of the  code, I also setted up connections between MainModel, MainView and MainCotroller and updated the archetecture during development. Me and Daniel created `draw_block()`, I created `_move(self, direction)`, `_rotate(self, direction)`, `read_event(self, event)` and participated in making `_rotate(direction)` with Daniel in [MainController](https://github.com/ArturAzarskyy/DOOMFALL####MainController). In [MainModel](https://github.com/ArturAzarskyy/DOOMFALL####MainModel) i create functions `is_at_the_bottom(self)`, ` request_draw(self)`, and modified `get_leftmost(self)`, `get_rightmost(self)`.
 - Abdul Aleem:
 	-
 - Chi Fung Chan:
 	-
 

# License
This project is licensed under the GNU GENERAL PUBLIC LICENSE License - see the [LICENSE.md](LICENSE.md) file for details

[Back to top](https://github.com/ArturAzarskyy/DOOMFALL#DOOMFALL)
