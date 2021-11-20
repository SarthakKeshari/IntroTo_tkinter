from tkinter import *

root = Tk()

e = Entry(root,width=50,bg="pink",fg="white",borderwidth=10)
e.pack()
e.insert(0,"Enter your name")


def myClick():
    hello = "Hello "+e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


myButton1 = Button(root, text="Enter Your Name", command=myClick, fg="red", bg="yellow")
myButton1.pack()


root.mainloop()