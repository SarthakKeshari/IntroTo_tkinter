from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Adding Frame')
root.iconbitmap('icon.jpg')

frame = LabelFrame(root,text="This is my frame...",padx=5,pady=5)
frame.pack(padx=10,pady=10)

b = Button(frame,text="Don't Click Here")
b.grid(row=0,column=0)
b2 = Button(frame,text="Don't Click Here")
b2.grid(row=1,column=1)

frame1 = LabelFrame(root,padx=5,pady=5)
frame1.pack(padx=10,pady=10)

b5 = Button(frame1,text="Don't Click Here")
b5.grid(row=0,column=0)
b4 = Button(frame1,text="Don't Click Here")
b4.grid(row=1,column=1)

root.mainloop()
