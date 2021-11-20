from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('Base')
root.iconbitmap('icon.jpg')


def open():
    global my_img
    root.filename = filedialog.askopenfilename(initialdir="/Images",title="Select a File",filetypes=(("png files","*.png"),("All files","*.*")))
    my_label = Label(root,text=root.filename).pack()

    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_img).pack()
    

my_btn = Button(root,text="open File",command=open).pack()

mainloop()