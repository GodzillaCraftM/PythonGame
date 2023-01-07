from tkinter import Tk as makescreen, Canvas, PhotoImage
from random import randint

screen = makescreen()
screen.title("Geometry Dash")
screen.resizable(0,0)
screen.wm_attributes("-topmost",1)

canvas = Canvas(screen, width=1300, height=560)
canvas.pack()
screen.update()

rect0image = PhotoImage(file = 'rect0.png')
rect1image = PhotoImage(file = 'rect1.png')
ro00image = PhotoImage(file = 'ro00.png')
ro01image = PhotoImage(file = 'ro01.png')
ro02image = PhotoImage(file = 'ro02.png')
ro03image = PhotoImage(file = 'ro03.png')
ro04image = PhotoImage(file = 'ro04.png')
ro05image = PhotoImage(file = 'ro05.png')
ro06image = PhotoImage(file = 'ro06.png')
ro07image = PhotoImage(file = 'ro07.png')
ro08image = PhotoImage(file = 'ro08.png')
ro09image = PhotoImage(file = 'ro09.png')
ro10image = PhotoImage(file = 'ro10.png')
obsimage = PhotoImage(file = 'obstacle.png')

canvas.create_rectangle(0,0,1300,560, fill="white")
canvas.create_rectangle(0,0,1300,40, fill="green")
canvas.create_rectangle(0,520,1300,560, fill="green")

rect = canvas.create_image(170,490,image = rect0image)

spinlist = [rect0image, ro00image, ro01image, ro02image,
            ro03image, ro04image, ro05image, ro06image,
            ro07image, ro08image, ro09image, ro10image, rect1image]


index = 0
location = 'down'
def animation_rect() :
    global index, location
    if location == 'down' :
        index += 1
        canvas.move(rect, 0, -35)
        canvas.itemconfig(rect, image = spinlist[index])
        if index == 12 :
            location = 'up'
            return
        else :
            canvas.after(20, animation_rect)
    elif location == 'up' :
        index -= 1
        canvas.move(rect, 0, 35)
        canvas.itemconfig(rect, image = spinlist[index])
        if index == 0 :
            location = 'down'
            return
        else :
            canvas.after(20, animation_rect)

direction = 'right'
def move_rect():
    pos = canvas.coords(rect)
    if pos [0]>0 and pos[0]<1300:
        if direction == 'left':
            canvas.move(rect, -7, 0)
        else :
            canvas.move(rect, 7, 0)
    canvas.after(10, move_rect)
move_rect()

score = 0
text = canvas.create_text(650, 280, text = '0',
                          font=('consolas', 150),fill='gray')
def setscore(number):
    global score
    score = number
    canvas.itemconfig(text, text = str(score))


def jump(event):
    setscore(score+1)
    animation_rect()
   
def left(event):
    global direction
    direction = 'left'
   
def right(event):
    global direction
    direction = 'right'

canvas.bind_all('<KeyPress-s>', jump)
canvas.bind_all('<KeyPress-Left>', left)
canvas.bind_all('<KeyPress-Right>', right)

obstaclelist = []
def create_obstacle():
    n = randint(0,1)
    y = 0
    if n == 0 :
        y = 460
    else:
        y = 100
    obstacle = canvas.create_image(1400,y,image=obsimage)
    obstaclelist.append(obstacle)
    canvas.after(500,create_obstacle)
create_obstacle()


def iscrush(opos):
    rpos = canvas.coords(rect)
    if rpos[0]-opos[0]>60:
        return False
    elif opos[0]-rpos[0]>60:
        return False
    elif rpos[1]-opos[1]>60:
        return False
    elif opos[1]-rpos[1]>60:
        return False
    else:
        return True
    

def move_obstacle() :
    for o in obstaclelist :
        canvas.move(o, -4-(score/10), 0)
        opos = canvas.coords(o)
        if opos[0] < 0 :
            obstaclelist.remove(o)
            canvas.delete(o)
        if iscrush(opos) :
            exit()
    canvas.after(10, move_obstacle)
move_obstacle()





screen.mainloop()
