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

    screen.draw.textbox(splitquestions[0],display,color="black")
    screen.draw.textbox(splitquestions[1],button1,color="black")
    screen.draw.textbox(splitquestions[2],button2,color="black")
    screen.draw.textbox(splitquestions[3],button3,color="black")
    screen.draw.textbox(splitquestions[4],button4,color="black")



def update():
    global timeramount
    if banner.x>=1280:
        banner.x=-1280
    banner.x=banner.x+2

def skipquestion():
    global timeramount
    if timeramount>0 and len(questions)>0:
        readsplit()
        timeramount=10
    else:
        endgame()

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
splitquestions=[]

storefile=open(questionfile,"r")
for i in storefile:
    print(i)
    questions.append(i)
print(questions)

def readsplit():
    global questions
    global splitquestions
    random.shuffle(questions)
    poppedquestions=questions.pop(0)
    splitquestions=poppedquestions.split(",") 
    
readsplit()

timeramount=(10)

def timerchange():
    global timeramount
    if timeramount>0:
        timeramount=timeramount-1

def on_mouse_down(pos):
    if skip.collidepoint(pos):
        skipquestion()
    elif button1.collidepoint(pos):
        if splitquestions[5]==1: 
            answerquestion()
        else:
            answerquestion()
    elif button2.collidepoint(pos): 
        if splitquestions[5]==2:
            answerquestion()   
        else:
            answerquestion()
    elif button3.collidepoint(pos): 
        if splitquestions[5]==3:
            answerquestion()
        else:
            answerquestion()
    elif button4.collidepoint(pos): 
        if splitquestions[5]==4:
            answerquestion()
        else:
            answerquestion()

def endgame():
    pass


clock.schedule_interval(timerchange,1)

pgzrun.go()
