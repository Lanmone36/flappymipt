import random
import pygame as pg
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Professor(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        
        #raw_image = pg.image.load("assets/player.png").convert_alpha()
        #self.image = pg.transform.scale(raw_image, (50, 50))
        self.image = pg.Surface((30, 30))
        self.image.fill((255, 0, 0))

        self.rect = self.image.get_rect()

    def update(self):
        pass
