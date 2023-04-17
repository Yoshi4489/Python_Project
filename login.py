import sqlite3
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('Sign in')

connect = sqlite3.connect('Login Database')

c = connect.cursor()

'''
c = connect.execute("""CREATE TABLE login_data(
                    first_name text,
                    last_name text,
                    gmail text,
                    user_name text,
                    password text,
                    phone_number intiger
                    )
                    """)
'''


def submit():
    # If State
    if f_name.get() == '':
        messagebox.showerror('Error', 'PLease Enter Your First Name')
    if l_name.get() == '':
        messagebox.showerror('Error', 'Please Enter Your Last Name')
    if gmail.get() == '':
        messagebox.showerror('Error', 'Please Enter Your Gmail')
    if user_name.get() == '':
        messagebox.showerror('Error', 'Please Enter Your User Name')
    if password.get() == '':
        messagebox.showerror('Error', 'Please Enter Your Password')
    if phone_number.get() == '':
        messagebox.showerror('Error', 'Please Enter Your Phone Number')
    elif f_name.get() and l_name.get() and gmail.get() and user_name.get() and password.get() and phone_number.get() != '':
        phone_num = phone_number.get()
        gmail_user = gmail.get()
        password_user = password.get()
        if gmail_user[-10:] != '.gmail.com':
            if gmail_user[-12:] != '.hotmail.com':
                messagebox.showerror(
                    'Error', 'Please Enter Your Email \nExamples .gmail.com .hotmail.com')
        if len(phone_num) == 10:
            try:
                int(phone_num)
            except ValueError:
                messagebox.showerror(
                    'Error', 'Phone Number Can Only Be Number')
                phone_number.delete(0, END)
        elif len(phone_num) != 10:
            messagebox.showerror('Error', "Phone Number Contain 10 Number")
        if len(password_user) < 8:
            messagebox.showwarning(
                'Warning', 'Password Contain Atleast 8 Charactor')
        elif gmail_user[-10:] == '.gmail.com':
            if int(phone_num) == int:
                print(phone_num)
                f_name.delete(0, END)
                l_name.delete(0, END)
                gmail.delete(0, END)
                user_name.delete(0, END)
                password.delete(0, END)
                phone_number.delete(0, END)
                messagebox.showinfo('Sign In', 'Sign In Successfully')
                window.destroy()

        elif gmail_user[-12:] == '.hotmail.com':
             if int(phone_num) == int:
                print(phone_num)
                f_name.delete(0, END)
                l_name.delete(0, END)
                gmail.delete(0, END)
                user_name.delete(0, END)
                password.delete(0, END)
                phone_number.delete(0, END)
                messagebox.showinfo('Sign In', 'Sign In Successfully')
                window.destroy()

    connect = sqlite3.connect('Login Database')

    c = connect.cursor()

    c.execute("INSERT INTO login_data VALUES (:f_name, :l_name, :gmail, :user_name, :password, :phone_number)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'gmail': gmail.get(),
                  'user_name': user_name.get(),
                  'password': password.get(),
                  'phone_number': phone_number.get(),
              })

    c = connect.commit()

    c = connect.close()


# Create Enter Box
f_name = Entry(window, width=30, border=5)
f_name.grid(row=0, column=1)
l_name = Entry(window, width=30, border=5)
l_name.grid(row=1, column=1)
gmail = Entry(window, width=30, border=5)
gmail.grid(row=2, column=1)
user_name = Entry(window, width=30, border=5)
user_name.grid(row=3, column=1)
password = Entry(window, width=30, border=5)
password.grid(row=4, column=1)
phone_number = Entry(window, width=30, border=5)
phone_number.grid(row=5, column=1)

# Create Label
f_name_label = Label(window, text='First Name')
f_name_label.grid(row=0, column=0)
l_name_label = Label(window, text='Last Name')
l_name_label.grid(row=1, column=0)
gmail_label = Label(window, text='Gmail')
gmail_label.grid(row=2, column=0)
user_name_label = Label(window, text='Username')
user_name_label.grid(row=3, column=0, padx=0)
password_label = Label(window, text='Password')
password_label.grid(row=4, column=0)
phone_number_label = Label(window, text='Phone Number')
phone_number_label.grid(row=5, column=0)

# Create Submit Button
submit_btn = Button(window, text='Sign In', width=38, command=submit)
submit_btn.grid(row=6, column=0, columnspan=2)

c = connect.commit()

c = connect.close()

window.mainloop()
