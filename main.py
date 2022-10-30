import pygame
import random
from constants import *


def main():
    pygame.init()
    screen_size = (WINDOW_WIDTH, WINDOW_HEIGHT)

    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Whac-A-Mole")

    # Initialization values
    squirrel_location = rand_squirrel_location()
    finish = False
    carrots_left = CARROTS_NUM_START

    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # press on X -> exit
                finish = True
            elif event.type == pygame.MOUSEBUTTONDOWN:  # clicked on the screen -> check if there is a hit
                squirrel_location = rand_squirrel_location()

        # Adding the objects on screen
        set_background(GREEN, screen)
        for carrots in range(carrots_left):
            add_image(CARROT_IMAGE, START_X_POS_CAR + SPACE_X_POS_CAR * carrots,
                      Y_POS_CAR, CARROT_WIDTH, CARROT_HEIGHT, screen)
        for hole in range(3):  # the top half of the hole
            add_image(HOLE_IMAGE, START_X_POS_HOL + SPACE_X_POS_HOL * hole,
                      Y_POS_HOL, HOLE_WIDTH, HOLE_HEIGHT, screen)
        add_image(SQUIRREL_IMAGE, squirrel_location[0], squirrel_location[1],
                  SQUIRREL_WIDTH, SQUIRREL_HEIGHT, screen)

        pygame.display.flip()

    pygame.quit()


def set_background(color, screen):
    screen.fill(color)


def add_image(img_path, x_pos, y_pos, width, height, screen):
    img = pygame.image.load(img_path)
    img = pygame.transform.scale(img, (width, height))
    screen.blit(img, (x_pos, y_pos))


def rand_squirrel_location():
    return [START_X_POS_SQU + random.randrange(3) * SPACE_X_POS_SQU,
            START_Y_POS_SQU]


main()
