import pygame as pg
from random import randint
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT

#добавить PROF_SPEED, указать постоянную скорость мобов.
#добавить GAP, чтобы не было рандомных чисел (19 строка)

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

        if self.rect.right <= 0: #going off-screen
            self.kill() #cleaning up resources
