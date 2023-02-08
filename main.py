import pygame
import sys

pygame.init()
from level import Level
from settings import *

level = Level()

while True:
    # Event Loop
    for event in pygame.event.get():
        # Close game if the windows X button is pressed
        if (
            event.type == pygame.QUIT
            or event.type == pygame.KEYDOWN
            and event.key == pygame.K_ESCAPE
        ):
            pygame.quit()
            sys.exit()

    SCREEN.fill(BACKGROUND_COLOUR)
    level.run()

    pygame.display.update()
    clock.tick(tickrate)
