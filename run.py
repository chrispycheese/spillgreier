import pygame as pg  
import numpy as np
from random import randint

def randomColor()->tuple[int]:
    return (randint(0,256),randint(0,256),randint(0,256))

def random2DPointOnScreen(screen:pg.Surface)->tuple:
    tup=screen.get_size()
    xCoord=int(np.random.uniform()*tup[0])#I want the position on the screen to be random. 
    yCoord=int(np.random.uniform()*tup[1])
    return (xCoord,yCoord)#I imagine that there are some advantages with having it as a tuple. 

def randomCircleSize():
    return 30+10*np.random.normal()#I want the radius to be centered around 30 with some spread.
    #This isnt controlling that I may make circles with negative sizes. 
    #This is not common because it is 3 standard deviations out of normal,
    #but I may have to find a better distribution that doesnt create negatives, like the poisson.

def drawCircleOnScreen(screen:pg.Surface)->None:
    pg.draw.circle(screen,randomColor(),random2DPointOnScreen(screen),randomCircleSize())

def run():
    pg.init()
    clock=pg.time.Clock()

    screen = pg.display.set_mode((400,400))#The first number is left-right and the second is up-down. 

    
    done=False

    while not done:
        for event in pg.event.get():  
            if event.type == pg.QUIT:  
                done = True 
            if event.type == pg.KEYDOWN:
                dealWithPressed(event)
                #print(event.key) I am not using this one. 

        drawCircleOnScreen(screen)
        #get the radius in here.


        pg.display.update()
        clock.tick(5)

def dealWithPressed(event):
    if event.key == pg.K_LEFT:
        print("hi")
    if event.key == pg.K_RIGHT:
        print("howdi")

run()