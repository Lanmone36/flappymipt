import pygame as pg
from random import randint
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Professor(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        
        #raw_image = pg.image.load("assets/player.png").convert_alpha()
        #self.image = pg.transform.scale(raw_image, (50, 50))
        self.image = pg.Surface((30, 30))
        self.image.fill((255, 0, 0))

        self.rect = self.image.get_rect()

        self.rect.bottomleft = (SCREEN_WIDTH+50,randint(self.rect.height,SCREEN_HEIGHT))

        self.speed = randint(5,12)

    def update(self):
        self.rect.x -= self.speed

    def draw(self, screen):
        self.draw.rect(screen, (255,0,0), self.rect)

