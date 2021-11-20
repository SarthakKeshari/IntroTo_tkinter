from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('Base')
root.iconbitmap('icon.jpg')
# root.geometry('400x400')


# # Create table
# c.execute("""CREATE TABLE addresses(
#     first_name text,
#     last_name text,
#     address text,
#     city text,
#     state text,
#     zipcode integer
#     )""")

# Create Submit Function for database
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create Cursor
    c = conn.cursor()

    # Insert Into table
    c.execute("INSERT INTO addresses VALUES (:f_name,:l_name,:address,:city,:state,:zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': int(zipcode.get())
              }
              )


    # Commit changes
    conn.commit()

    # Close connection
    conn.close()



    # Clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


# Create Query Function
def query():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create Cursor
    c = conn.cursor()

    # Query the database
    c.execute("SELECT oid,* FROM addresses")
    records = c.fetchall()
    # print(records)
    print_records=''
    # print_records='ID\tFirst Name\tLast Name\tAddress\tCity\tState\tZipcode\n'

    for record in records:
        one_record=''
        for data in record:
            one_record+=str(data)+'\t'
        print_records += str(one_record) + '\n'

    query_label = Label(root,text=print_records)
    query_label.grid(row=8,column=0,columnspan=2)

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()




# Create Text Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=4, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

# Create Text Box Labels
f_name_label = Label(root, text="First name")
f_name_label.grid(row=0, column=0)

l_name_label = Label(root, text="Last name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

# Create Submit Button
submit_btn = Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Query Button
query_btn = Button(root,text="Show Records",command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=150)

mainloop()
