import pygame
from settings import *
from tile import Tile
from player import Player


class Level:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = pygame.sprite.Group()
        self.active_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        self.setup_level()

    def setup_level(self) -> None:
        for row_index, row in enumerate(LEVEL_MAP):
            for column_index, column in enumerate(row):
                x = column_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if column == "X":
                    Tile((x, y), [self.visible_sprites, self.collision_sprites])
                elif column == "P":
                    Player(
                        (x, y),
                        [self.visible_sprites, self.active_sprites],
                        self.collision_sprites,
                    )

    def run(self) -> None:
        self.active_sprites.update()
        self.visible_sprites.draw(self.display_surface)
