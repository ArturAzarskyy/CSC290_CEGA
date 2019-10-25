import pygame

from src.Game import MainController, MainModel

pygame.init()


# We can create a list of shape cordinates
def run_game():
    game = MainModel.MainModel()
    controller = MainController.MainController(game)


    game_height = 800 # Size of the squeares will be aproximetly 40
    game_width =  400 # It is based that the grid is 10  * 20
    screen_width = 600

    size = 40

    #From here
    start_x = game_width/2
    start_y = 0

    curr_y = 40 # The bottom of the block
    curr_x = start_x

    previous_position = None
    next_position = [(0, 0), (160, 0), (160, 40), (0, 40)] #this is for the cordinates of the block currently this is
    #used as example
    #Till here are suposed to be recived from model

    win = pygame.display.set_mode((screen_width, game_height))

    pygame.draw.line(win, (0, 255, 0), (game_width, 0), (game_width, game_height), 1)
    isRunning = True
    while isRunning:
        pygame.time.delay(1900)# this value will be received from the model
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            else:
                controller.read_event(event)

    # we would probably get position in the grid form the model and multiply every coordinate by the size of the block

        previous_position = draw_block(win, previous_position, next_position)
        # pygame.draw.polygon(win, (255, 0, 0), [(0, curr_y - 40), (160, curr_y - 40), (160, curr_y), (0, curr_y)])

        if curr_y != 800:
            curr_y += 40
            print(curr_y) #this functionality will be in model class

        next_position = [(0, curr_y - 40), (160, curr_y - 40), (160, curr_y), (0, curr_y)]

        pygame.display.update()
    # This is just me experimenting with movement of the block down to see how it might work
    # Feel free to un-comment this small portion and see how it works

    pygame.quit()

def draw_block(pygame_window, previous_position, new_position):
    """
    This function imitates the effect that the block is falling.

    This is achieved by drawing previous position in color of background.
    :param pygame_window: enviorment where to draw the the block
    :param previous_position: Array of (x, y) coordinates going clockwise. Which indicate the last position of the block
    :param new_position: Array of (x, y) coordinates  going clockwise. Which represent where to draw the block next
    :return: Array of (x, y) points used 
    """
    if previous_position is None:
        pygame.draw.polygon(pygame_window, (255,0,0), new_position)
    else:
        pygame.draw.polygon(pygame_window, (0,0,0), previous_position)
        pygame.draw.polygon(pygame_window, (255,0,0), new_position)

    return new_position


if __name__ == "__main__":
    run_game()