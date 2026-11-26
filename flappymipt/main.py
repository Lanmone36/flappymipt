import pygame as pg

##### SCREEN SETTINGS #####
SCREEN_WIDTH = 800
SCREEN_HEIGTH = 600

SCREEN_CAPTION = "FlappyMIPT"

FPS = 60

##### MAIN #####
def main():
    pg.init()

    pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
    pg.display.set_caption(SCREEN_CAPTION)

    clock = pg.time.Clock()

    run = True
    while run:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                run = False

        clock.tick(FPS)
        
    pg.quit()


if __name__ == "__main__":
    main()