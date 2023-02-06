import pygame, time, os

clock = pygame.time.Clock()
last_time = time.time()
tickrate = 60
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

FLAGS = pygame.DOUBLEBUF | pygame.HWSURFACE
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), FLAGS)
SCREEN.set_alpha(None)

game_font = pygame.font.Font("Fonts/Pixeltype.ttf", 20)
