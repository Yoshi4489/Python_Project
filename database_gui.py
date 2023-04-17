from tkinter import *
import sqlite3

root = Tk()
root.title('Database')
root.geometry('300x400')

#Database

# Create a Database or connect to server
connect_1 = sqlite3.connect('Database')

# Create cursor
c = connect_1.cursor()

# Create Table
# Disable the execute cuz we don't want to  create it again CREATE ONLY ONCE
"""
c.execute('''CREATE TABLE adresses (
first_name text, 
last_name text,
adress text,
city text,
state text,
zipcode intiger
)''')
"""

def update():
    # Create a Database or connect to server
    connect_1 = sqlite3.connect('Database')

    # Create cursor
    c = connect_1.cursor()
    
    record_id = delete_enter.get()
    c.execute("""UPDATE adresses SET
            first_name = :first,
            last_name = :last,
            adress = :adress,
            city = :city,
            state = :state,
            zipcode = :zipcode
            
            WHERE oid = :oid""",
            {'first' : f_name_editor.get(),
             'last' : l_name_editor.get(),
             'adress' : adress_editor.get(),
             'city' : city_editor.get(),
             'state' : state_editor.get(),
             'zipcode' : zipcode_editor.get(),
             'oid' : record_id
            }
            )
 
    # Commit Changes
    connect_1.commit()

    #Close Connect
    connect_1.close()
    
    editor.destroy()

# Create Edit Function
def edit():
    global editor
    editor = Tk()
    editor.title('Update A Record')
    editor.geometry('400x600')
    
    # Create a Database or connect to server
    connect_1 = sqlite3.connect('Database')

    # Create cursor
    c = connect_1.cursor()
     
    record_id = delete_enter.get()
    # Query the Database
    c.execute("SELECT * FROM adresses WHERE oid=" + record_id)
    records = c.fetchall()
        
    # Loop thru Results
    print_record = ''
    for record in records:
        # record จะเป็นของมูลของแต่ละบุคคล record[0 คือ first name] record[1 คือ last name] record[-1 คือ id]
        print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + str(record[-1]) + '\n'

    # Create Global variables for text box names
    global f_name_editor
    global l_name_editor
    global adress_editor
    global city_editor
    global state_editor 
    global zipcode_editor

    # Create Enter
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20)

    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)

    adress_editor = Entry(editor, width=30)
    adress_editor.grid(row=2, column=1, padx=20)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)

    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)

    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1,  padx=20)

    # Create Label
    f_name_label = Label(editor, text='First name')
    f_name_label.grid(row=0, column=0)

    l_name_label = Label(editor, text='Last name')
    l_name_label.grid(row=1, column=0)

    adress_label = Label(editor, text='Adress')
    adress_label.grid(row=2, column=0)

    city_label = Label(editor, text='City')
    city_label.grid(row=3, column=0)

    state_label = Label(editor, text='State')
    state_label.grid(row=4, column=0)

    zipcode_label = Label(editor, text='Zipcode')
    zipcode_label.grid(row=5, column=0)
  
    # Loop thru Results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        adress_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])
    
    # Create a Save Button To Save edited record
    save_button = Button(editor, text='Save Record', command=update)
    save_button.grid(row=6, column=0, columnspan=2, ipadx=92, pady=10, padx=0)
    
    # Commit Changes
    connect_1.commit()

    #Close Connect
    connect_1.close()

# Create Function to Delete a record
def delete():
    # Create a Database or connect to server
    connect_1 = sqlite3.connect('Database')

    # Create cursor
    c = connect_1.cursor()
    
    # Delete a record
    # ลบข้อมูลจากเลข oidที่รับค่ามาจาก delete_enter.get() ค่าเป็น str
    c.execute("DELETE from adresses WHERE oid=" + delete_enter.get())
    
    # Commit Changes
    connect_1.commit()

    #Close Connect
    connect_1.close()

# Create Submit Function
def submit():
    # Create a Database or connect to server
    connect_1 = sqlite3.connect('Database')

    # Create cursor
    c = connect_1.cursor()
    
    # Insert Into Database
    c.execute("INSERT INTO adresses VALUES (:f_name, :l_name, :adress,:city, :state, :zipcode)",
              {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'adress': adress.get(),
                'city': city.get(),
                'state': state.get(),
                'zipcode': zipcode.get()
              }
        )
    
    # Commit Changes
    connect_1.commit()

    #Close Connect
    connect_1.close()

    # Clear The Text Box
    f_name.delete(0, END)
    l_name.delete(0, END)
    adress.delete(0, END)
    state.delete(0, END)
    city.delete(0, END)
    zipcode.delete(0, END)

# Query The Database
def query():
    # Create a Database or connect to server
    connect_1 = sqlite3.connect('Database')

    # Create cursor
    c = connect_1.cursor()

    # Query The Data
    # * mean EVERYTHING, oid mean ORIGINSL ID (เลขท้ายสุด)
    c.execute('SELECT *, oid  FROM adresses')
    records = c.fetchall()
    print(records)
    
    print_record = ''
    # Loop thru
    # ใน records จะเป็น List ที่เก็บข้อมูลของทุกคนไว้
    for record in records:
        # record จะเป็นของมูลของแต่ละบุคคล record[0 คือ first name] record[1 คือ last name] record[-1 คือ id]
        print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + str(record[-1]) + '\n'
        
    query_label = Label(root, text=print_record)
    query_label.grid(row=12, column=0, columnspan=2)

    # Commit Changes
    connect_1.commit()

    #Close Connect
    connect_1.close()

# Create Enter
f_name  = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

adress = Entry(root, width=30)
adress.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1,  padx=20)

delete_enter = Entry(root)
delete_enter.grid(row=9, column=1)

# Create Label
f_name_label = Label(root, text='First name')
f_name_label.grid(row=0, column=0)

l_name_label = Label(root, text='Last name')
l_name_label.grid(row=1, column=0)

adress_label = Label(root, text='Adress')
adress_label.grid(row=2, column=0)

city_label = Label(root, text='City')
city_label.grid(row=3, column=0)

state_label = Label(root, text='State')
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text='Zipcode')
zipcode_label.grid(row=5, column=0)

delete_label = Label(root, text='ID Number')
delete_label.grid(row=9, column=0)

# Create a Submit button
submit_button = Button(root, text='Add Record To Database', command=submit)
submit_button.grid(row=6, column=0, columnspan=2, padx=0, ipadx=57, pady=10)

# Create a query button
query_button = Button(root, text='Show Records', command=query)
query_button.grid(row=7, column=0, columnspan=2, padx=0, ipadx=84, pady=10)

# Create a  Delete button
delete_button = Button(root, text='Delete Record', command=delete)
delete_button.grid(row=10, column=0, columnspan=2, ipadx=85, pady= 10)

# Create an Update button
update_button = Button(root, text='Edit Record', command=edit)
update_button.grid(row=11, column=0, columnspan=2, ipadx=92, pady= 10)

# Commit Changes
connect_1.commit()

#Close Connect
connect_1.close()

root.mainloop()
