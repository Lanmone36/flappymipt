import pygame as pg
from random import randint
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Professor(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        
        #raw_image = pg.image.load("assets/player.png").convert_alpha()
        #self.image = pg.transform.scale(raw_image, (50, 50))
