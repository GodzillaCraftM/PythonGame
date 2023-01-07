from tkinter import Tk as makescreen, Canvas, PhotoImage
from random import randint
import winsound

screen= makescreen()
screen.title("Bricks Jump Game")
screen.resizable(0,0)
screen.wm_attributes("-topmost", 1)

canvas = Canvas(screen, width=800,height=800)
canvas.pack()
screen.update()

canvas.create_rectangle(0,0,800,800,fill = 'white')

ball = canvas.create_oval(100,10,150,60,fill = 'hot pink')

yspeed = 0
xspeed = 10
gravity = 1

def moveball():
  global xspeed,yspeed,gravity
  canvas.move(ball, xspeed, yspeed)
  yspeed += gravity

  ballpos = canvas.coords(ball)
  if ballpos[3]>800:
    yspeed= -30
  if ballpos[0]<5 or ballpos[2]>795:
    xspeed *= -1
  canvas.after(50, moveball)
moveball()

blocklist = []

makeblocks():
  for x in range(0, 701, 100):
    color = randint(0,1)
    if color == 0:
      color = 'black'
    elif color == 1:
      color = 'red'
    block = canvas.create_rectangle(x,800,x+99,850,fill=color)
    blocklist.append(block)
  canvas.after(2000,makeblocks)
makeblocks()

def moveblocks():
  for blocks in blocklist:
    canvas.move(block,0,-1)
  canvas.after(10,moveblocks)
moveblocks()

def right(event):
  for index in range(0,len(blocklist),1):
    canvas.move(blocklist[index],100,0)
  for index in range(7,len(blocklist),8):
    canvas.move(blocklist[index],-800,0)
    blocklist.insert(index-7,blocklist[index])
    del(blocklist[index+1])


screen.mainloop()
