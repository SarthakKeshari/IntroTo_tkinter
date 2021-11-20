from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Base')
root.iconbitmap('icon.jpg')

var = StringVar()

def show():
    my_label = Label(root, text=var.get()).pack()


c = Checkbutton(root,text="Check 1",variable = var,command=show, onvalue="On",offvalue="Off")
c.deselect()
c.pack()


mainloop()