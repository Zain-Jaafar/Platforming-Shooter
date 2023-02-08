import pygame
import sys

pygame.init()
# from level import level
# from player import player
from settings import *

while True:
    SCREEN.fill((0, 0, 0))

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

    pygame.display.update()
    clock.tick(tickrate)
