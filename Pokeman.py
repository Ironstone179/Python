from tkinter import *
from random import *

def main():
    global d
    c.delete(start)

    def move(ce,name):
        dire = randint(0,3)
        if dire == 0 and ce[1]>60:
            c.move(name, 0, -80)
            root.after(400, move(ce,name))
        elif dire == 1 and ce[3]<740:
            c.move(name, 0, 80)
            root.after(400, move(ce,name))
        elif dire == 2 and ce[2]<740:
            c.move(name, 80, 0)
            root.after(400, move(ce,name))
        elif dire == 3 and ce[0]>60:
            c.move(name, -80, 0)
            root.after(400, move(ce,name))
        else:
            move(ce,name)
        
    def key(event):
        global count1, count2, count3
        coo = c.coords('player')
        ce1 = c.coords('enemy1')
        ce2 = c.coords('enemy2')
        ce3 = c.coords('enemy3')
        ce4 = c.coords('enemy4')
        if event.keysym == 'Left' and coo[0]>20:
            c.move('player',-10,0)
        elif event.keysym == 'Right' and coo[2]<780:
            c.move('player',10,0)
        elif event.keysym == 'Up' and coo[1]>20:
            c.move('player',0,-10)
        elif event.keysym == 'Down' and coo[3]<780:
            c.move('player',0,10)
        elif event.keysym == 'Down' and coo[0]>360 and coo[2]<440 and count1>0 and count2>0 and count3>0:
            c.move('player',0,10)
        if count1>0 and count2>0 and count3>0:
            c.delete(gate)

        if b1[0]==coo[0] and b1[1]==coo[1]:
            c.itemconfig(but1,fill='green')
            coo1 = c.coords('but1')
            count1+=1
        if b2[0]==coo[0] and b2[1]==coo[1]:
            c.itemconfig(but2,fill='green')
            coo2 = c.coords('but2')
            count2+=1
        if b3[0]==coo[0] and b3[1]==coo[1]:
            c.itemconfig(but3,fill='green')
            coo3 = c.coords('but3')
            count3+=1
    
        if coo[3] == 800:
            c.itemconfig(won,fill='yellow')
            c.delete(enemy1)
            c.delete(enemy2)
            c.delete(enemy3)
            c.delete(enemy4)
            c.delete(circle)
        if (coo[0]-ce1[0])*(coo[0]-ce1[0])+(coo[1]-ce1[1])*(coo[1]-ce1[1])<=1800 or (coo[0]-ce2[0])*(coo[0]-ce2[0])+(coo[1]-ce2[1])*(coo[1]-ce2[1])<=1800 or (coo[0]-ce3[0])*(coo[0]-ce3[0])+(coo[1]-ce3[1])*(coo[1]-ce3[1])<=1800 or (coo[0]-ce4[0])*(coo[0]-ce4[0])+(coo[1]-ce4[1])*(coo[1]-ce4[1])<=1800:
            c.itemconfig(lose,fill='red')
            c.delete(enemy1)
            c.delete(enemy2)
            c.delete(enemy3)
            c.delete(enemy4)
            c.delete(circle)
            

    root.bind_all('<Key>', key)

    won = c.create_text(400,380, text='You won!', fill='black')
    lose = c.create_text(400,400, text='You`ve been poked!', fill='black')

    gate = c.create_line(360,790,440,790, fill='green', width=20)
    but1 = c.create_oval(60,380,100,420, fill='lime', outline='green', tag='but1')
    b1 = c.coords('but1')
    but2 = c.create_oval(380,60,420,100, fill='lime', outline='green', tag='but2')
    b2 = c.coords('but2')
    but3 = c.create_oval(700,380,740,420, fill='lime', outline='green', tag='but3')
    b3 = c.coords('but3')

    circle = c.create_oval(380,430,420,470, fill='yellow', outline='yellow', tag='player')
    coo = c.coords('player')

    enemy1 = c.create_oval(60,380,100,420, fill='red', outline='red', tag='enemy1')
    ce1 = c.coords('enemy1')
    name1 = 'enemy1'
    move(ce1,name1)
    enemy2 = c.create_oval(380,700,420,740, fill='red', outline='red', tag='enemy2')
    ce2 = c.coords('enemy2')
    #move(ce2)
    enemy3 = c.create_oval(700,380,740,420, fill='red', outline='red', tag='enemy3')
    ce3 = c.coords('enemy3')
    #move(ce3)
    enemy4 = c.create_oval(380,60,420,100, fill='red', outline='red', tag='enemy4')
    ce4 = c.coords('enemy4')
    #move(ce4)

d='darkblue'
count1=0
count2=0
count3=0
count4=0
root = Tk()
root.title('Pokeman')
root.resizable(0,0)
c = Canvas(root, width=800, height=800, bg='black')
c.pack()

lborder = c.create_rectangle([0,0],[20,800], fill=d, outline=d)
uborder = c.create_rectangle([0,0],[800,20], fill=d, outline=d)
rborder = c.create_rectangle([800,0],[780,800], fill=d, outline=d)
dborder1 = c.create_rectangle([0,800],[360,780], fill=d, outline=d)
dborder2 = c.create_rectangle([440,800],[800,780], fill=d, outline=d)

start = c.create_text(400,420, text='To win you must poke 3 green buttons and pass through the gate\n If you come too close to the red enemies they will poke you and you will lose, \n but if you`re not moving - they won`t be able to poke you \n Good luck!', fill='Yellow')
root.after(100, main)

root.mainloop()


