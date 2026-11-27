import pygame as pg

class Timer:
    timer = pg.time

    def __init__(self):
        self.finish = 0

    def start(self, time: int):
        self.finish = self.timer.get_ticks() + time

    def ready(self):
        return self.timer.get_ticks() >= self.finish