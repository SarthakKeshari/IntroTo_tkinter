from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Adding Frame')
root.iconbitmap('icon.jpg')

r = IntVar()
# r=StringVar()
r.set("2")
print(r.get())


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="Option 3", variable=r, value=3, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="Option 4", variable=r, value=4, command=lambda: clicked(r.get())).pack()

myLabel = Label(root, text=r.get())
myLabel.pack()

myButton = Button(root, text="Click Me!", command=lambda: clicked(r.get()))
myButton.pack()

root.mainloop()
