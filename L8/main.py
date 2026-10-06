import pgzrun, os

os.environ['SDL_VIDEO_CENTERED']='1'

WIDTH=1280
HEIGHT=720

def draw():
    screen.fill("lightyellow")
    screen.draw.filled_rect(banner,"blue")
    screen.draw.filled_rect(display,"darkgray")
    screen.draw.filled_rect(timer,"green")
    screen.draw.filled_rect(skip,"orange")
    screen.draw.filled_rect(button1,"red")
    screen.draw.filled_rect(button2,"red")
    screen.draw.filled_rect(button3,"red")
    screen.draw.filled_rect(button4,"red")


banner=Rect(0,0,1280,60)
display=Rect(10,70,960,120)
timer=Rect(980,70,290,120)
skip=Rect(980,200,290,510)
button1=Rect(10,200,400,250)
button2=Rect(500,200,400,250)
button3=Rect(10,460,400,250)
button4=Rect(500,460,400,250)


pgzrun.go()