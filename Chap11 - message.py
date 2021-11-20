from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title('Adding Frame')
root.iconbitmap('icon.jpg')

#showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.askyesno("This is my Popup","Hello World!")
    Label(root,text=response).pack()
    if response == 1:
        Label(root, text="You clicked YES").pack()
    else:
        Label(root, text="You clicked NO").pack()

Button(root,text="Popup",command=popup).pack()


mainloop()