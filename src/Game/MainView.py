import pygame

from src.Game import MainController, MainModel

pygame.init()

shape_size = 40
game_height = shape_size * 20
game_width = shape_size * 10
screen_width = 600
font = pygame.font.SysFont('Agency FB', 30)
big_font = pygame.font.SysFont('Agency FB', 48)  # Used only for "Game Over"
bg_color = (5, 5, 5)


# We can create a list of shape coordinates
class MainView:
    def run_game(self):
        game = MainModel.MainModel(self)
        controller = MainController.MainController(game)


        # EXAMPLE OF A BLOCK FALLING
        #From here
        start_x = game_width/2
        start_y = 0

        curr_y = 40 # The bottom of the block
        curr_x = start_x

        self.previous_position = None
        next_position = [(0, 0), (160, 0), (160, 40), (0, 40)] #this is for the cordinates of the block currently this is
        #used as example
        #Till here are suposed to be recived from model

        self.win = pygame.display.set_mode((screen_width, game_height))

        self.last = pygame.time.get_ticks()


        # Setup background
        self.win.fill(bg_color)
        self.draw_grid(self.win)
        self.draw_text(self.win, "SCORE", game_width+25, 5)
        self.draw_text(self.win, "LEVEL", game_width+25, 125)

        isRunning = True
        while isRunning:
            now = pygame.time.get_ticks()
            if now-self.last >= game.get_delay():
                self.last = now
                game.curr_y_pos += 1# this value will be received from the model

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        isRunning = False
                    else:
                        controller.read_event(event)

                # update score
                pygame.draw.polygon(self.win, bg_color,
                                    [(game_width + 25, 45), (game_width + 25, 85), (screen_width, 85), (screen_width, 45)])
                self.draw_text(self.win, str(game.get_score()), game_width+25, 45)
                pygame.draw.polygon(self.win, bg_color,
                                    [(game_width + 25, 165), (game_width + 25, 205), (screen_width, 205), (screen_width, 165)])
                self.draw_text(self.win, str(game.get_level()), game_width+25, 165)

                # EXAMPLE CONTINUED

                self.previous_position = self.draw_block(self.win, self.previous_position, game)
                # print(game._get_block_lowest())
                #TODO: is block at the bottom  then call function in MainModel To set that block in grid an to use next block
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        isRunning = False
                    else:
                        controller.read_event(event)
                pygame.draw.polygon(self.win, bg_color,
                                    [(game_width + 25, 45), (game_width + 25, 85), (screen_width, 85), (screen_width, 45)])
                self.draw_text(self.win, str(game.get_score()), game_width+25, 45)
                pygame.draw.polygon(self.win, bg_color,
                                    [(game_width + 25, 165), (game_width + 25, 205), (screen_width, 205), (screen_width, 165)])
                self.draw_text(self.win, str(game.get_level()), game_width+25, 165)

                # EXAMPLE CONTINUED

                self.previous_position = self.draw_block(self.win, self.previous_position, game)
                #TODO: is block at the bottom  then call function in MainModel To set that block in grid an to use next block

            pygame.display.update()

        pygame.quit()


    def draw_block(self, pygame_window, old_pos, game):
        """
        This function imitates the effect that the block is falling.
        This is achieved by drawing previous position in color of background.
        :param pygame_window: environment where to draw the the block
        :param previous_position: Tuple (x, y) coordinates which indicate the last position of the block
        :param game: this is the game in which the game is run, used to get the current coordinates of the block location as
                     well as the block dimensions
        :return: Tuple of (x, y) points used
        """
        #if previous_position is not None:
        #    pygame.draw.polygon(pygame_window, bg_color, previous_position)
        #pygame.draw.polygon(pygame_window, (255,0,0), new_position)
        # pygame.draw.rect(pygame_window, (255,0,0), (0,0,40,40))
        if old_pos is not None:
            for i in range(len(game.curr_block)):
                for j in range(len(game.curr_block[0])):
                    if game.curr_block[i][j] != 0:
                        pygame.draw.rect(pygame_window, bg_color,
                                         ((old_pos[0] + j) * 40, (old_pos[1] + i) * 40, 40, 40))

        for i in range(len(game.curr_block)):
            for j in range(len(game.curr_block[0])):
                if game.curr_block[i][j] != 0:
                    pygame.draw.rect(pygame_window, (255,0,0), ((game.get_leftmost() + j)*40, (game.get_botmost() + i)*40, 40, 40))

        self.draw_grid(pygame_window)

        return game.get_leftmost(), game.get_botmost()


    def draw_text(self,pygame_window, text, x, y):
        """
        This function draws some given text on the screen
        :param pygame_window: environment where to draw the text
        :param text: string to be printed
        :param x: the x-coordinate for where the string should be drawn
        :param y: the y-coordinate for where the string should be drawn
        :return: None
        """
        text = font.render(text, False, (169, 169, 169))
        pygame_window.blit(text, (x, y))


    def draw_grid(self, pygame_window):
        """
        This function draws a 10x20 grid
        :param pygame_window: environment where to draw the grid
        :return: None
        """
        # Draw Grid
        for i in range(shape_size, game_width, shape_size):
            pygame.draw.line(pygame_window, (169, 169, 169), (i, 0), (i, game_height), 1)
        for j in range(shape_size, game_height, shape_size):
            pygame.draw.line(pygame_window, (169, 169, 169), (0, j), (game_width, j), 1)
        pygame.draw.line(pygame_window, (0, 255, 0), (game_width, 0), (game_width, game_height), 1)


    def draw_end_game(self, pygame_window, final_score):
        """
        This function draws an overlay for the end game screen including the final score
        :param pygame_window: environment where to make a translucent screen and draw final_score
        :param final_score: final score that was reached by the player
        :return: None
        """
        s = pygame.Surface((game_width, game_height))
        s.set_alpha(128)
        s.fill((0,0,0))
        game_over_text = big_font.render("Game Over", False, (169, 169, 169))
        score_text = font.render("Final Score: " + str(final_score), False, (169, 169, 169))
        pygame_window.blit(s, (0,0))
        pygame_window.blit(game_over_text, (game_width/2 - (big_font.size("Game Over")[0]/2), game_height/3))
        pygame_window.blit(score_text, (game_width/2 - (font.size("Final Score: " + str(final_score))[0]/2), game_height/3 + 55))


if __name__ == "__main__":
    mainView = MainView()
    mainView.run_game()
