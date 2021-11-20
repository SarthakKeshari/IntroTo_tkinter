from tkinter import *

root = Tk()
root.title("Simple Calculator")

sum = 0
new_num_count=0
new_equation=0
math=""

e = Entry(root,width=50,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(number):
    global new_num_count
    if new_num_count==0:
        e.delete(0,END)
        new_num_count+=1
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))

def button_clear():
    e.delete(0,END)
    global sum
    global new_equation
    global math
    sum=0
    new_equation=0
    math=""

def button_equal():
    number = e.get()
    e.delete(0,END)
    if math=="addition":
        e.insert(0, sum+int(number))

    if math=="substraction":
        e.insert(0, sum-int(number))

    if math=="multiplication":
        e.insert(0, sum+int(number))

    if math=="division":
        e.insert(0, sum/int(number))


def button_add():
    global sum
    global math
    if math=="addition":
        e.insert(0, sum+int(number))

    if math=="substraction":
        e.insert(0, sum-int(number))

    if math=="multiplication":
        e.insert(0, sum+int(number))

    if math=="division":
        e.insert(0, sum/int(number))
    global new_num_count
    new_num_count = 0
    math = "addition"
    sum+=int(e.get())
    e.delete(0,END)
    e.insert(0, sum)

def button_sub():
    global sum
    global math
    if math=="addition":
        e.insert(0, sum+int(number))

    if math=="substraction":
        e.insert(0, sum-int(number))

    if math=="multiplication":
        e.insert(0, sum+int(number))

    if math=="division":
        e.insert(0, sum/int(number))
    global new_num_count
    new_num_count = 0
    math = "substraction"
    if new_equation==0:
        sum+=int(e.get())
        return
    sum-=int(e.get())
    e.delete(0,END)
    e.insert(0, sum)

def button_mul():
    global sum
    global math
    if math=="addition":
        e.insert(0, sum+int(number))

    if math=="substraction":
        e.insert(0, sum-int(number))

    if math=="multiplication":
        e.insert(0, sum+int(number))

    if math=="division":
        e.insert(0, sum/int(number))
    global new_num_count
    new_num_count = 0

    math = "multiplication"
    if new_equation==0:
        sum+=int(e.get())
        return
    sum*=int(e.get())
    e.delete(0,END)
    e.insert(0, sum)

def button_div():
    global sum
    global math
    if math=="addition":
        e.insert(0, sum+int(number))

    if math=="substraction":
        e.insert(0, sum-int(number))

    if math=="multiplication":
        e.insert(0, sum+int(number))

    if math=="division":
        e.insert(0, sum/int(number))
    global new_num_count
    new_num_count = 0
    math = "division"
    if new_equation==0:
        sum+=int(e.get())
        return
    sum/=int(e.get())
    e.delete(0,END)
    e.insert(0, sum)



#Define buttons
button_1 = Button(root,text="1",padx=40,pady=40,command=lambda: button_click(1))
button_2 = Button(root,text="2",padx=40,pady=40,command=lambda: button_click(2))
button_3 = Button(root,text="3",padx=40,pady=40,command=lambda: button_click(3))
button_4 = Button(root,text="4",padx=40,pady=40,command=lambda: button_click(4))
button_5 = Button(root,text="5",padx=40,pady=40,command=lambda: button_click(5))
button_6 = Button(root,text="6",padx=40,pady=40,command=lambda: button_click(6))
button_7 = Button(root,text="7",padx=40,pady=40,command=lambda: button_click(7))
button_8 = Button(root,text="8",padx=40,pady=40,command=lambda: button_click(8))
button_9 = Button(root,text="9",padx=40,pady=40,command=lambda: button_click(9))
button_0 = Button(root,text="0",padx=40,pady=40,command=lambda: button_click(0))

button_add = Button(root,text="+",padx=39,pady=40,command=button_add)
button_sub = Button(root,text="-",padx=40,pady=40,command=button_sub)
button_mul = Button(root,text="*",padx=40,pady=40,command=button_mul)
button_div = Button(root,text="/",padx=40,pady=40,command=button_div)
button_equal = Button(root,text="=",padx=40,pady=40,command=button_equal)
button_clear = Button(root,text="Clear",padx=30,pady=40,command=button_clear)

#Put buttons on screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_add.grid(row=3,column=3)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_sub.grid(row=2,column=3)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_mul.grid(row=1,column=3)

button_0.grid(row=4,column=0)
button_equal.grid(row=4,column=1)
button_clear.grid(row=4,column=2,columnspan=1)
button_div.grid(row=4,column=3)

root.mainloop()