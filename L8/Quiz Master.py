import pgzrun, os, random

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

    screen.draw.textbox("Welcome to Quiz Master!",banner,color="black")
    screen.draw.textbox("S\nK\nI\nP",skip,color="black",shadow=(0.5,0.5),scolor="gray")
    screen.draw.textbox(str(timeramount),timer,color="black",shadow=(0.5,0.5),scolor="gray")


def update():
    global timeramount
    if banner.x>=1280:
        banner.x=-1280
    banner.x=banner.x+2



banner=Rect(0,0,1280,60)
display=Rect(10,70,960,120)
timer=Rect(980,70,290,120)
skip=Rect(980,200,290,510)
button1=Rect(10,200,475,250)
button2=Rect(495,200,475,250)
button3=Rect(10,460,475,250)
button4=Rect(495,460,475,250)

questions=[]
questionfile=(r"C:\Users\Satwik\Desktop\Python\L8\Quiz Master questions.txt")

storefile=open(questionfile,"r")
for i in storefile:
    print(i)
    questions.append(i)
print(questions)

def readsplit():
    global questions
    random.shuffle(questions)
    poppedquestions=questions.pop(0)
    
    

timeramount=(10)

def timerchange():
    global timeramount
    if timeramount>0:
        timeramount=timeramount-1

clock.schedule_interval(timerchange,1)

pgzrun.go()