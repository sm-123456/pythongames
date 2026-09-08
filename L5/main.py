import pgzrun 
from random import randint 

WIDTH=1000
HEIGHT=650
score=0

Alien=Actor("flower")
Alien.pos=(500,325)
Astronaut=Actor("bee")
Astronaut.pos=(120,150)


def draw():
    global gameover
    screen.fill("white")
    Alien.draw()
    Astronaut.draw()
    screen.draw.text(f"Score: {score}", (10, 10), fontsize=30, color="black")
    if gameover==True:
        screen.fill("grey")
        screen.draw.text(f"Game Over\nFinal score: {score}", (450, 300), fontsize=30, color="black")   

gameover=False

def end():
    global gameover
    gameover=True

def update(): 
    global score
    if keyboard.left or keyboard.a: 
        Astronaut.x=Astronaut.x-10
    if keyboard.right or keyboard.d: 
        Astronaut.x=Astronaut.x+10
    if keyboard.up or keyboard.w: 
        Astronaut.y=Astronaut.y-10
    if keyboard.down or keyboard.s: 
        Astronaut.y=Astronaut.y+10
    if Alien.colliderect(Astronaut):
        score+=1
        while True:
            Num1=randint(100,900)
            Num2=randint(100,550)
            Alien.pos=(Num1,Num2)
            if not Alien.colliderect(Astronaut):
                break
clock.schedule(end,10)
        
pgzrun.go()