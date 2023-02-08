import pygame, os

clock = pygame.time.Clock()
tickrate = 60

TILE_SIZE = 64
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

FLAGS = pygame.DOUBLEBUF | pygame.HWSURFACE
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), FLAGS)
pygame.display.set_caption("Platforming Shooter")

game_font = pygame.font.Font(os.path.join("Fonts/Pixeltype.ttf"), 20)

BG_COLOUR = "#060C17"
PLAYER_COLOUR = "#C4F7FF"
TILE_COLOUR = "#94D7F2"

CAMERA_BORDERS = {"left": 100, "right": 200, "top": 100, "bottom": 150}

LEVEL_MAP = [
    "                         ",
    "                         ",
    "                         ",
    "        XXX       XX     ",
    "  P                      ",
    "XXXXX        XX        XX",
    "XXXX       XX            ",
    "X     X  XXXX   XX  XX   ",
    "      X  XXXX   XX  XXX  ",
    "   XXXX  XXXXXX XX  XXXX ",
    "XXXXXXX  XXXXXX XX  XXXX ",
]
