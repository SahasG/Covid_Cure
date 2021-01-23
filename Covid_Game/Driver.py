from Covid_Game import Game_State
import pygame as pg

pg.init()
WIDTH = HEIGHT = 512
Frames = 30

def draw(screen, state):
    drawBack(screen)
    drawState(screen, state.screen)

def drawBack(screen):
    pg.draw.rect(screen, "gray", pg.Rect(0, 0, WIDTH, HEIGHT))

def drawState(screen, state.screen):
    pass

def main():
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    screen.fill(pg.Color("white"))
    state = Game_State.State()
    running = True
    while running  == True:
        for event in pg.event.get():
            if(event.type == pg.QUIT):
                running = False
            elif(event.type == pg.MOUSEBUTTONDOWN):
                pass
            draw(screen, state)
            clock.tick(Frames)
            pg.display.flip()
