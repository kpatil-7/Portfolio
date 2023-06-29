from tkinter import *
import random, time

root = Tk()
root.title('Images over image tkinter canvas')
root.resizable(width=False, height=False)
root.geometry('+750+150')
root.geometry('500x400')
root.configure(bg='SystemButtonFace')
roadImage = PhotoImage(file='road.png')
stickman200 = PhotoImage(file='stickman200.png')
stickman100 = PhotoImage(file='stickman100.png')
stickman50 = PhotoImage(file='stickman50.png')

canvas1 = Canvas(root, width=500, height=400)
canvas1.pack()
background = canvas1.create_image(0, 0, anchor=NW, image=roadImage)

while True:
    number = random.choice([1, 2, 3])
    if number == 1:
        manOnRoad1 = canvas1.create_image(230, 150, anchor=NW, image=stickman200)
        root.update_idletasks()
        root.update()
        time.sleep(1)
        canvas1.delete(manOnRoad1)
    elif number == 2:
        manOnRoad2 = canvas1.create_image(240, 40, anchor=NW, image=stickman100)
        root.update_idletasks()
        root.update()
        time.sleep(1)
        canvas1.delete(manOnRoad2)
    else:
        manOnRoad3 = canvas1.create_image(190, 30, anchor=NW, image=stickman50)
        root.update_idletasks()
        root.update()
        time.sleep(1)
        canvas1.delete(manOnRoad3)

root.mainloop()
