import pygame as pg
from time import strftime as now

SCREEN = WIDTH, HEIGHT = 1920, 1080
CENTER = WIDTH // 2, HEIGHT // 2

BG = (20, 20, 20)


def main():
    pg.font.init()

    sc = pg.display.set_mode(SCREEN)
    font = pg.font.SysFont('arial', 340, True)

    pg.event.clear()
    pg.event.set_blocked(None)
    pg.event.set_allowed(pg.KEYUP)

    sc.fill(BG)
    pg.display.update()

    while True:
        pg.time.delay(100)  # 10 FPS
        [exit() for event in pg.event.get() if event.key == pg.K_ESCAPE]

        render = font.render(now('%H : %M : %S'), True, 'white', BG)
        rect = render.get_rect(center=CENTER)

        sc.blit(render, rect)

        pg.display.update(rect)


if __name__ == '__main__':
    main()
