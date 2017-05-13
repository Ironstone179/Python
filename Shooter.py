from tkinter import *

window = Tk()
window.title('Shooter')
canvas = Canvas(width='560', height='600', bg='darkgreen')
canvas.pack()

def shoot():
    global load

    c = canvas.coords('player')
    canvas.create_line(c[0]+5,c[1],c[0]+5,c[1]+10,width=5,fill='black',tag='bullet')
    load = 0

    move_bullet('bullet')


def move_bullet(name):
    global load

    canvas.move(name,0,-20)

    if load == 0:
        bc = canvas.coords(name)

        for i in enemies:

            ec = canvas.coords(i)

            if ec[0] <= bc[0] <= ec[0] + 60:
                if bc[1] <= ec[1] + 60:
                    canvas.delete(i)
                    enemies.remove(i)
                    canvas.delete(name)
                    load = 1
                    if len(enemies)==0:
                        canvas.create_text(300,300,text='You won!', fill = 'white', font='Arial 30')
                    
                    
        if bc[1] < 0: 
            canvas.delete(name)
            load = 1

    if load == 0:
        window.after(50, move_bullet, 'bullet')

def press(event):
    global load

    c = canvas.coords('player')

    if event.keysym == 'Left' and c[0] > 0:
        canvas.move("player", -20,0)
    elif event.keysym == 'Right' and c[2] < 600:
        canvas.move("player", 20, 0)
    elif event.keysym == 'space' and load == 1:
        shoot()

def create_enemy():
    global enemies

    enemies = []

    for x in range(7):
        for y in range (3):
            enemy = canvas.create_rectangle(10 + 80 * x, 10 + 80 * y, 70 + 80 * x , 70 + 80 * y, fill='white', outline='white', tag='enemy')
            enemies.append(enemy)

def move_enemy():
    canvas.move('enemy', 0, 20)
    c =canvas.coords('player')
    for i in enemies:

            ec = canvas.coords(i)

            if ec[3] >= c[1]:
                canvas.delete('player')
                canvas.create_text(300,300,text='You lost!', fill = 'black', font='Arial 30')
                
    window.after(1000, move_enemy)


canvas.create_rectangle(295,550,305,600,fill='white',outline='white',tag='player')

load = 1

create_enemy()
move_enemy()
window.bind_all('<Key>', press)

window.mainloop()
