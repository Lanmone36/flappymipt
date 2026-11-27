import pygame as pg
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT
from src.settings import INIT_POS, GRAVITY_BOOST, FLAP_SPEED, MAX_SPEED, INIT_SPEED


class Stird(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()

        #raw_image = pg.image.load("assets/player.png").convert_alpha()
        #self.image = pg.transform.scale(raw_image, (50, 50))
        self.image = pg.Surface((40, 40))
        self.image.fill((0, 0, 255))

        self.rect = self.image.get_rect()
        self.rect.center = INIT_POS

        self.speed = INIT_SPEED

        self.flappy = False

    def flap(self):
        self.speed = FLAP_SPEED

    def update(self):
        self.rect.y += self.speed
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.rect.top = 0
            self.speed = 0

        self.speed = min(self.speed + GRAVITY_BOOST, MAX_SPEED)
