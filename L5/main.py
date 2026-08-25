import pgzrun 

WIDTH=1000
HEIGHT=650

Alien=Actor("alien")
Alien.pos=(500,325)
Astronaut=Actor("screenshot 2026-08-18 175945")
Astronaut.pos=(120,150)


def draw():
    screen.fill("darkgray")
    Alien.draw()
    Astronaut.draw()

def update(): 
    if keyboard.left: 
        Astronaut.x=Astronaut.x-10
    if keyboard.right: 
        Astronaut.x=Astronaut.x+10





pgzrun.go()