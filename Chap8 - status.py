from tkinter import *

# Importing library for accessing images
from PIL import ImageTk, Image

root = Tk()
root.title('IMAGES - ICONS - EXIT BUTTONS')
root.iconbitmap('icon.jpg')

my_img1 = ImageTk.PhotoImage(Image.open('Screenshot (3).png'))
my_img2 = ImageTk.PhotoImage(Image.open('Screenshot (4).png'))
my_img3 = ImageTk.PhotoImage(Image.open('Screenshot (5).png'))
my_img4 = ImageTk.PhotoImage(Image.open('Screenshot (6).png'))

image_list = [my_img1, my_img2, my_img3, my_img4]

list_length = len(image_list)
image_number = 0

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


def back(img_num):
    global my_label
    global image_number
    global list_length
    image_number -= 1
    if image_number < 0:
        image_number = list_length - 1

    img_num = image_number

    # Updating label
    my_label.grid_forget()
    my_label = Label(image=image_list[img_num])
    my_label.grid(row=0, column=0, columnspan=3)

    # Updating Status bar
    status = Label(root, text="Image " + str(image_number + 1) + " of " + str(list_length), bd=1, relief=SUNKEN,
                   anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


def forward(img_num):
    global my_label
    global image_number
    global list_length
    image_number += 1
    if image_number >= list_length:
        image_number = 0

    img_num = image_number

    # Updating label
    my_label.grid_forget()
    my_label = Label(image=image_list[img_num])
    my_label.grid(row=0, column=0, columnspan=3)

    # Updating Status bar
    status = Label(root, text="Image " + str(image_number + 1) + " of " + str(list_length), bd=1, relief=SUNKEN,
                   anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


button_back = Button(root, text="<<", command=lambda: back(image_number))
button_quit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(image_number))

status = Label(root, text="Image " + str(image_number + 1) + " of " + str(list_length), bd=1, relief=SUNKEN, anchor=E)
status.grid(row=2, column=0, columnspan=3, sticky=W + E)

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1, pady=10)
button_forward.grid(row=1, column=2)

root.mainloop()
