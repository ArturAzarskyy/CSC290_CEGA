import pygame

from src.Game import MainController, MainModel

pygame.init()


# We can create a list of shape cordinates
def run_game():
    game_height = 800 # Size of the squeares will be aproximetly 40
    game_width =  400 # It is based that the grid is 10  * 20
    screen_width = 600

    size = 40

    #From here
    start_x = game_width/2
    start_y = 0

    curr_y = 40 # The bottom of the block
    curr_x = start_x
    #Till here

    game = MainModel.MainModel()
    controller = MainController.MainController(game)

    win = pygame.display.set_mode((screen_width, game_height))

    isRunning = True
    while isRunning:
        pygame.time.delay(1900)# this value will be received from the model
        win.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            else:
                controller.read_event(event)

    # we would probably get position in the grid form the model and multiply every coordinate by the size of the block

        pygame.draw.line(win,(0,255,0), (game_width,0), (game_width, game_height),1)
        pygame.draw.polygon(win, (255, 0, 0), [(0, curr_y - 40), (160, curr_y - 40), (160, curr_y), (0, curr_y)])

        if curr_y != 800:
            curr_y += 40
            print(curr_y)

        pygame.display.update()
    # This is just me experimenting with movement of the block down to see how it might work
    # Feel free to un-comment this small portion and see how it works

    pygame.quit()

if __name__ == "__main__":
    run_game()