from tkinter import *
from random import *
        
def key(event):
    cp2 = c.coords('player2')
    if event.keysym == 'a' and cp2[0]>0:
        c.move('player2', -10,0)
    elif event.keysym == 'd' and cp2[2] < 500:
        c.move('player2', 10, 0)

    cp1 = c.coords('player1')
    if event.keysym == 'Left' and cp1[0]>0:
        c.move('player1', -10,0)
    elif event.keysym == 'Right' and cp1[2] < 500:
        c.move('player1', 10, 0)

def move():
    global vx,vy,point,start,text
    start.place(x=1000,y=1000)
    c.delete(text)
    c.move('ball',vx,vy)
    cor = c.coords('ball')
    co1 = c.coords('player1')
    co2 = c.coords('player2')
    x = cor[0]+10
    window.after(50,move)
    if cor[2]>=500 or cor[0]<=0:
        vx = -vx
    if (cor[1]<=50 and x>=co2[0] and x<=co2[2]) or (cor[3]>=500 and x>=co1[0] and x<=co1[2]):
        vy = -vy
        point += 1
    if cor[1]>=550:
        print(point)
        c.create_text(250,225,text='Player 2 lost the ball!', fill = 'red', font='Arial 30')
        c.create_text(250,250,text='Look in Shell to check, how many points you earned', fill = 'yellow', font='Arial 15')
        c.delete('ball')
    if cor[3]<=0:
        print(point)
        c.create_text(250,225,text='Player 1 lost the ball!', fill = 'red', font='Arial 30')
        c.create_text(250,250,text='Look in Shell to check, how many points you earned', fill = 'yellow', font='Arial 15')
        c.delete('ball')

window = Tk()
window.title('Pong')
window.resizable(0,0)
c = Canvas(width='500', height='550', bg = 'black')
c.pack()

text=c.create_text(250,270,text='Player 1 uses buttons "a" and "d" to move\n Player 2 uses buttons "Left" and "Right" to move', fill = 'yellow', font='Arial 15')
start = Button(window, text='Start', command = move)
start.place(x=230,y=400)

point = 0

c.create_rectangle(215,500,285,510, fill='grey', tag='player1')
c.create_rectangle(215,40,285,50, fill='grey', tag='player2')
window.bind_all('<Key>', key)

c.create_oval(240,215,260,235, fill='white', tag='ball')
direction = randint(0,1)

cor = c.coords('ball')

r = 10
x = cor[0]+10
y = cor[1]+10
vx = randint(-10,10)
vy = randint(-10,10)

window.mainloop()

