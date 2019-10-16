import pygame

pygame.init()

game_height = 800 # Size of the squeares will be aproximetly 40
game_width =  400 # It is based that the grid is 10  * 20



size = 40

start_x = game_width/2
start_y = 0

curr_y = 40 # The bottom of the block
curr_x = start_x


win = pygame.display.set_mode((game_width, game_height))

run = True

# We can create a list of shape cordinates
while run:
    pygame.time.delay(1900);
    win.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    # we would probably get position in the grid form the model and multiply every coordinate by the size of the block

    # pygame.draw.polygon(win, (255, 0, 0), [(0, curr_y - 40), (160, curr_y - 40), (160, curr_y), (0, curr_y)])
    #
    # if curr_y != 800:
    #     curr_y += 40
    #     print(curr_y)


    pygame.display.update()

    # This is just me experimenting with movement of the block down to see how it might work
    # Feel free to un-comment this small portion and see how it works

pygame.quit()

