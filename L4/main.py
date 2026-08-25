from random import randint

import pgzrun

WIDTH=600
HEIGHT=400

TITLE="Catch the alien!"

alex=Actor("alien")
alex.pos=(300,200)

def draw():
    screen.fill("darkgray")
    alex.draw()
    screen.draw.text(f"Score: {score}", (10, 10), fontsize=30, color="white")

def on_mouse_down(pos):
    if alex.collidepoint(pos):
        global score
        score+=1
        alex.pos=(randint(0,WIDTH),randint(0,HEIGHT))



score=0
pgzrun.go() 