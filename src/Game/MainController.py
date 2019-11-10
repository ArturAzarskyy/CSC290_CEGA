import pygame

class MainController:

    def __init__(self, game):
        self.game = game


    def read_event(self, event ):
        """
        Method used to determine what should be done when user precessed
        keyboard key.

        :param event: pygame event
        :return: None
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self._move(-1)
            elif event.key == pygame.K_d:
                self._move(1)
            elif event.key == pygame.K_q:
                self._rotate(-1)
            elif event.key == pygame.K_e:
                self._rotate(1)
        return None


    def _rotate(self, direction):
        # if direction == -1:
            # self.game.move_block_left()
        # else:
            # self.game.move_block_right()
        return None

    def _move(self, direction):
        if direction == -1:
            self.game.move_block_left()
        else:
            self.game.move_block_right()