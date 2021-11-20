from tkinter import *

#Importing library for accessing images
from PIL import ImageTk,Image

root = Tk()
root.title('IMAGES - ICONS - EXIT BUTTONS')

root.iconbitmap('icon.jpg')

my_img = ImageTk.PhotoImage(Image.open('icon.jpg'))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root,text="Exit Program",command=root.quit)
button_quit.pack()


root.mainloop()