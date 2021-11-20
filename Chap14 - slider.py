from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Base')
root.iconbitmap('icon.jpg')
root.geometry('400x400')

def slide(abc):
    root.geometry('400x'+str(vertical.get()))

vertical = Scale(root, from_=0,to=200,command=slide)
vertical.pack()

horizontal = Scale(root, from_=0,to=400,orient=HORIZONTAL)
horizontal.pack()

def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get())+'x400')

my_label = Label(root,text=horizontal.get()).pack()

my_btn = Button(root,text="Click Me!",command=slide).pack()

mainloop()