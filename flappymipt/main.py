import pygame as pg
from random import randint

from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_CAPTION, SCREEN_BACKGROUND
from src.settings import FPS
from src.settings import PROF_MIN_SPAWN_TIME, PROF_MAX_SPAWN_TIME, PROF_DELAY_SPAWN_TIME

from src.timer import Timer

from src.sprites.stird import Stird
from src.sprites.professor import Professor


##### MAIN #####
def main():
    pg.init()

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption(SCREEN_CAPTION)

    bg_raw = pg.image.load(SCREEN_BACKGROUND).convert()
    background = pg.transform.scale(bg_raw, (SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pg.time.Clock()

    ##### SPRITES #####
    sprites = pg.sprite.Group()
    professors = pg.sprite.Group() #it's needed to handle collisions with professors!

    stird = Stird()
    sprites.add(stird)

    prof_spawn_timer = Timer()
    prof_spawn_timer.start(randint(PROF_MAX_SPAWN_TIME - PROF_DELAY_SPAWN_TIME, PROF_MAX_SPAWN_TIME))

    run = True
    while run:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                run = False

            ##### Stird's processing #####
            if e.type == pg.KEYDOWN:
                if e.key in (pg.K_SPACE, pg.K_UP):
                    stird.flap()
            if e.type == pg.MOUSEBUTTONDOWN and e.button == 1:
                stird.flap()

        ##### UPDATING #####
        if prof_spawn_timer.ready(): #spawning professors
            prof = Professor()
            sprites.add(prof)
            professors.add(prof)
        
            prof_spawn_timer.start(randint(PROF_MIN_SPAWN_TIME, PROF_MAX_SPAWN_TIME))
        
        sprites.update()

        if pg.sprite.spritecollide(stird, professors, False):
            print("Touching prof!")

        ##### DRAWING #####
        screen.blit(background, (0, 0))
        sprites.draw(screen)
        pg.display.flip()

        clock.tick(FPS)
        
    pg.quit()


if __name__ == "__main__":
    main()