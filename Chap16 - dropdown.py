from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Base')
root.iconbitmap('icon.jpg')
root.geometry('400x400')
root.resizable(0,0)


def show(abc):
    Label(root,text=clicked.get()).pack()

options = ["Mon","Tue","Wed","Thur","Fri","Sat","Sun"]

clicked = StringVar()
clicked.set(options[0])
drop = OptionMenu(root, clicked,*options,command=show).pack()


mainloop()