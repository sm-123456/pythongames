import pgzrun 
from random import randint 

WIDTH=1000
HEIGHT=650
score=0

Apple=Actor("apple1 (custom)")
Apple.pos=(500,100)
Basket=Actor("basket1 (custom)")
Basket.pos=(500,530)

def draw():
    screen.fill("grey")
    Apple.draw()
    Basket.draw()
    screen.draw.text(f"Score: {score}", (10, 10), fontsize=30, color="black")


def update(): 
    global score
    if keyboard.left or keyboard.a: 
        Basket.x=Basket.x-10
        if Basket.x<=0:
            Basket.x=0
    if keyboard.right or keyboard.d: 
        Basket.x=Basket.x+10
        if Basket.x>=1000:
            Basket.x=1000
    Apple.y=Apple.y+5
    if Apple.y>=670:
        num1=randint(50,950)
        Apple.pos=(num1,-20)
    if Apple.colliderect(Basket):
        score+=1
        num1=randint(50,950)
        Apple.pos=(num1,-20)
        
pgzrun.go()