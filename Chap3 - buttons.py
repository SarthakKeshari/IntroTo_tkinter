from tkinter import *

root = Tk()


def myClick():
    myLabel = Label(root, text="I clicked a button")
    myLabel.pack()


myButton1 = Button(root, text="Click Me!", command=myClick, fg="red", bg="yellow")
myButton1.pack()

myButton2 = Button(root, text="Click Me!", state=DISABLED)
myButton2.pack()

myButton3 = Button(root, text="Click Me!", padx=50, pady=50)
myButton3.pack()

root.mainloop()
