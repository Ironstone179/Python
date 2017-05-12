from tkinter import *
from random import *

def draw_x1():
    global r1,c1,c2,c3,c4,c5,c6,c7,c8,c9,count,finish
    if c1==0:
        c1=c1+1
        co = c.coords(r1)
        c.create_line(co[0],co[1],co[2],co[3], capstyle='round', fill='red', width='20')
        c.create_line(co[0],co[3],co[2],co[1], capstyle='round', fill='red', width='20')
        if (c1+c2+c3==3 or c1+c4+c7==3 or c1+c5+c9==3 or c4+c5+c6==3 or c7+c8+c9==3 or c7+c5+c3==3 or c2+c5+c8==3 or c3+c6+c9==3) and finish==0:
            c.create_text(670, 150, text='You won!', font='Arial 20', fill='green')
            finish=1
        root.after(100,draw_o)
        count+=1

def draw_x2():
    global r2,c1,c2,c3,c4,c5,c6,c7,c8,c9,count,finish
    if c2==0:
        c2=c2+1
        co = c.coords(r2)
        c.create_line(co[0],co[1],co[2],co[3], capstyle='round', fill='red', width='20')
        c.create_line(co[0],co[3],co[2],co[1], capstyle='round', fill='red', width='20')
        if (c1+c2+c3==3 or c1+c4+c7==3 or c1+c5+c9==3 or c4+c5+c6==3 or c7+c8+c9==3 or c7+c5+c3==3 or c2+c5+c8==3 or c3+c6+c9==3) and finish==0:
            c.create_text(670, 150, text='You won!', font='Arial 20', fill='green')
            finish=1
        root.after(100,draw_o)
        count+=1
    
def draw_x3():
    global r3,c1,c2,c3,c4,c5,c6,c7,c8,c9,count,finish
    if c3==0:
        c3=c3+1
        co = c.coords(r3)
        c.create_line(co[0],co[1],co[2],co[3], capstyle='round', fill='red', width='20')
        c.create_line(co[0],co[3],co[2],co[1], capstyle='round', fill='red', width='20')
        if (c1+c2+c3==3 or c1+c4+c7==3 or c1+c5+c9==3 or c4+c5+c6==3 or c7+c8+c9==3 or c7+c5+c3==3 or c2+c5+c8==3 or c3+c6+c9==3) and finish==0:
            c.create_text(670, 150, text='You won!', font='Arial 20', fill='green')
            finish=1
        root.after(100,draw_o)
        count+=1
    
def draw_x4():
    global r4,c1,c2,c3,c4,c5,c6,c7,c8,c9,count,finish
    if c4==0:
        c4=c4+1
        co = c.coords(r4)
        c.create_line(co[0],co[1],co[2],co[3], capstyle='round', fill='red', width='20')
        c.create_line(co[0],co[3],co[2],co[1], capstyle='round', fill='red', width='20')
        if (c1+c2+c3==3 or c1+c4+c7==3 or c1+c5+c9==3 or c4+c5+c6==3 or c7+c8+c9==3 or c7+c5+c3==3 or c2+c5+c8==3 or c3+c6+c9==3) and finish==0:
            c.create_text(670, 150, text='You won!', font='Arial 20', fill='green')
            finish=1
        root.after(100,draw_o)
        count+=1
    
def draw_x5():
    global r5,c1,c2,c3,c4,c5,c6,c7,c8,c9,count,finish
    if c5==0:
        c5=c5+1
        co = c.coords(r5)
        c.create_line(co[0],co[1],co[2],co[3], capstyle='round', fill='red', width='20')
        c.create_line(co[0],co[3],co[2],co[1], capstyle='round', fill='red', width='20')
        if (c1+c2+c3==3 or c1+c4+c7==3 or c1+c5+c9==3 or c4+c5+c6==3 or c7+c8+c9==3 or c7+c5+c3==3 or c2+c5+c8==3 or c3+c6+c9==3) and finish==0:
            c.create_text(670, 150, text='You won!', font='Arial 20', fill='green')
            finish=1
        root.after(100,draw_o)
        count+=1

def draw_x6():
    global r6,c1,c2,c3,c4,c5,c6,c7,c8,c9,count,finish
    if c6==0:
        c6=c6+1
        co = c.coords(r6)
        c.create_line(co[0],co[1],co[2],co[3], capstyle='round', fill='red', width='20')
        c.create_line(co[0],co[3],co[2],co[1], capstyle='round', fill='red', width='20')
        if (c1+c2+c3==3 or c1+c4+c7==3 or c1+c5+c9==3 or c4+c5+c6==3 or c7+c8+c9==3 or c7+c5+c3==3 or c2+c5+c8==3 or c3+c6+c9==3) and finish==0:
            c.create_text(670, 150, text='You won!', font='Arial 20', fill='green')
            finish=1
        root.after(100,draw_o)
        count+=1
    
def draw_x7():
    global r7,c1,c2,c3,c4,c5,c6,c7,c8,c9,count,finish
    if c7==0:
        c7=c7+1
        co = c.coords(r7)
        c.create_line(co[0],co[1],co[2],co[3], capstyle='round', fill='red', width='20')
        c.create_line(co[0],co[3],co[2],co[1], capstyle='round', fill='red', width='20')
        if (c1+c2+c3==3 or c1+c4+c7==3 or c1+c5+c9==3 or c4+c5+c6==3 or c7+c8+c9==3 or c7+c5+c3==3 or c2+c5+c8==3 or c3+c6+c9==3) and finish==0:
            c.create_text(670, 150, text='You won!', font='Arial 20', fill='green')
            finish=1
        root.after(100,draw_o)
        count+=1
    
def draw_x8():
    global r8,c1,c2,c3,c4,c5,c6,c7,c8,c9,count,finish
    if c8==0:
        c8=c8+1
        co = c.coords(r8)
        c.create_line(co[0],co[1],co[2],co[3], capstyle='round', fill='red', width='20')
        c.create_line(co[0],co[3],co[2],co[1], capstyle='round', fill='red', width='20')
        if (c1+c2+c3==3 or c1+c4+c7==3 or c1+c5+c9==3 or c4+c5+c6==3 or c7+c8+c9==3 or c7+c5+c3==3 or c2+c5+c8==3 or c3+c6+c9==3) and finish==0:
            c.create_text(670, 150, text='You won!', font='Arial 20', fill='green')
            finish=1
        root.after(100,draw_o)
        count+=1
    
def draw_x9():
    global r9,c1,c2,c3,c4,c5,c6,c7,c8,c9,count,finish
    if c9==0:
        c9=c9+1
        co = c.coords(r9)
        c.create_line(co[0],co[1],co[2],co[3], capstyle='round', fill='red', width='20')
        c.create_line(co[0],co[3],co[2],co[1], capstyle='round', fill='red', width='20')
        if (c1+c2+c3==3 or c1+c4+c7==3 or c1+c5+c9==3 or c4+c5+c6==3 or c7+c8+c9==3 or c7+c5+c3==3 or c2+c5+c8==3 or c3+c6+c9==3) and finish==0:
            c.create_text(670, 150, text='You won!', font='Arial 20', fill='green')
            finish=1
        root.after(100,draw_o)
        count+=1

def draw_o():
    global c1,c2,c3,c4,c5,c6,c7,c8,c9,count,finish
    rand = randint(0,8)
    if rand == 0 and c1==0:
        c1+=4
        x1=20
        y1=20
    elif rand == 1 and c2==0:
        c2+=4
        x1=220
        y1=20
    elif rand == 2 and c3==0:
        c3+=4
        x1=420
        y1=20
    elif rand == 3 and c4==0:
        c4+=4
        x1=20
        y1=220
    elif rand == 4 and c5==0:
        c5+=4
        x1=220
        y1=220
    elif rand == 5 and c6==0:
        c6+=4
        x1=420
        y1=220
    elif rand == 6 and c7==0:
        c7+=4
        x1=20
        y1=420
    elif rand == 7 and c8==0:
        c8+=4
        x1=220
        y1=420
    elif rand == 8 and c9==0:
        c9+=4
        x1=420
        y1=420
    else:
        draw_o()
        
    c.create_oval(x1,y1,x1+160,y1+160,fill='white',outline='blue',width='20')
    
    if (c1+c2+c3==12 or c1+c4+c7==12 or c1+c5+c9==12 or c4+c5+c6==12 or c7+c8+c9==12 or c7+c5+c3==12 or c2+c5+c8==12 or c3+c6+c9==12) and finish==0:
        c.create_text(670, 150, text='You lost!', font='Arial 20', fill='red')
        finish=1
    count+=1

root = Tk()
root.resizable(0,0)
root.title('Cross-Zero')
c = Canvas(root, width=750, height=600, bg='black')
c.pack()

c1,c2,c3,c4,c5,c6,c7,c8,c9,count,finish=0,0,0,0,0,0,0,0,0,0,0

r1 = c.create_rectangle([20,20],[180,180],fill='white')
r2 = c.create_rectangle([220,20],[380,180],fill='white')
r3 = c.create_rectangle([420,20],[580,180],fill='white')
r4 = c.create_rectangle([20,220],[180,380],fill='white')
r5 = c.create_rectangle([220,220],[380,380],fill='white')
r6 = c.create_rectangle([420,220],[580,380],fill='white')
r7 = c.create_rectangle([20,420],[180,580],fill='white')
r8 = c.create_rectangle([220,420],[380,580],fill='white')
r9 = c.create_rectangle([420,420],[580,580],fill='white')

b1 = Button(root, text='UL(1)', command=draw_x1)
b1.pack()
b1.place(x=600,y=240)
b2 = Button(text='UM(2)', command=draw_x2)
b2.pack()
b2.place(x=650,y=240)
b3 = Button(text='UR(3)', command=draw_x3)
b3.pack()
b3.place(x=700,y=240)
b4 = Button(text='ML(4)', command=draw_x4)
b4.pack()
b4.place(x=600,y=290)
b5 = Button(text='MM(5)', command=draw_x5)
b5.pack()
b5.place(x=650,y=290)
b6 = Button(text='MR(6)', command=draw_x6)
b6.pack()
b6.place(x=700,y=290)
b7 = Button(text='DL(7)', command=draw_x7)
b7.pack()
b7.place(x=600,y=340)
b8 = Button(text='DM(8)', command=draw_x8)
b8.pack()
b8.place(x=650,y=340)
b9 = Button(text='DR(9)', command=draw_x9)
b9.pack()
b9.place(x=700,y=340)

root.mainloop()




























# P.S: Вылетающие под конец работы программы ошибки - не баг, а фича
