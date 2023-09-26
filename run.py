import pygame as pg  

def run():
    pg.init()
    screen = pg.display.set_mode((400,400))
    done=False
    while not done:
        for event in pg.event.get():  
            if event.type == pg.QUIT:  
                done = True  
    pg.display.flip()
run()