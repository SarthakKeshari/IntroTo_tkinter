from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Base')
root.iconbitmap('icon.jpg')


def open():
    top = Toplevel()
    top.title('Second Window')
    global my_img
    my_img = ImageTk.PhotoImage(Image.open('Screenshot (3).png'))
    lbl = Label(top, image=my_img).pack()
    btn2 = Button(top,text="Close Window", command=top.destroy).pack()

btn = Button(root, text="Open Second Window", command=open).pack()


mainloop()
