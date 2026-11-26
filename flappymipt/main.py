import pygame as pg


from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_CAPTION, SCREEN_BACKGROUND
from src.settings import FPS

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

    ##### Sprites #####
    sprites = pg.sprite.Group()
    professors = pg.sprite.Group()

    stird = Stird()
    sprites.add(stird)

    for _ in range(10):
        professor = Professor()
        sprites.add(professor)
        professors.add(professor)

    run = True
    while run:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                run = False

            stird.handler(e)

        ##### UPDATING #####
        sprites.update()

        if pg.sprite.spritecollide(stird, professors, False):
            pass

        ##### DRAWING #####
        screen.blit(background, (0, 0))
        sprites.draw(screen)
        pg.display.flip()

        clock.tick(FPS)
        
    pg.quit()


if __name__ == "__main__":
    main()