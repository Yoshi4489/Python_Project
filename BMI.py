from tkinter import *
from tkinter import messagebox

window = Tk()


def BMI():
    m = height_enter.get()
    kg = weight_enter.get()
    kg = int(kg)
    m = int(m) / 100
    if m == 0:
        messagebox.showwarning('Your BMI', 'Height cant be 0 you LIAR!!')
    average = kg / (m * m)
    average = round(average, 2)
    if average <= 0:
        question = messagebox.askyesno('BMI', 'Do you want to know your BMI?')
        if question == 0:
            while question == 0:
                question = messagebox.askyesno('BMI', 'Do you want to know your BMI?')
                if question == 1:
                    messagebox.showinfo('Your BMI', f'Your BMI : {average} You are no longer HUMAN!!!')
        elif question == 1:
            messagebox.showinfo('Your BMI', f'Your BMI : {average} You are no longer HUMAN!!!')
    elif average <= 18.49:
        question = messagebox.askyesno('BMI', 'Do you want to know your BMI?')
        if question == 0:
            while question == 0:
                question = messagebox.askyesno('BMI', 'Do you want to know your BMI?')
                if question == 1:
                    messagebox.showinfo('Your BMI', f'Your BMI : {average} You are Underweight')
        elif question == 1:
            messagebox.showinfo('Your BMI', f'Your BMI : {average} You are Underweight')
    elif 18.5 <= average <= 24.9:
        question = messagebox.askyesno('BMI', 'Do you want to know your BMI?')
        if question == 0:
            while question == 0:
                question = messagebox.askyesno('BMI', 'Do you want to know your BMI?')
                if question == 1:
                    messagebox.showinfo('Your BMI', f'Your BMI : {average} You are Normal weight')
        elif question == 1:
            messagebox.showinfo('Your BMI', f'Your BMI : {average} You are Normal weight')
    elif 25 <= average <= 29.9:
        question = messagebox.askyesno('BMI', 'Do you want to know your BMI?')
        if question == 0:
            while question == 0:
                question = messagebox.askyesno('BMI', 'Do you want to know your BMI?')
                if question == 1:
                    messagebox.showinfo('Your BMI', f'Your BMI : {average} You are Overweight')
        elif question == 1:
            messagebox.showinfo('Your BMI', f'Your BMI : {average} You are Overweight')
    elif average >= 30:
        question = messagebox.askyesno('BMI', 'Do you want to know your BMI?')
        if question == 0:
            while question == 0:
                question = messagebox.askyesno('BMI', 'Do you want to know your BMI?')
                if question == 1:
                    messagebox.showinfo('Your BMI', f'Your BMI : {average} You are Obesity')
        elif question == 1:
            messagebox.showinfo('Your BMI', f'Your BMI : {average} You are Obesity')
    weight_enter.delete(0, END)
    height_enter.delete(0, END)


def clear():
    question = messagebox.askyesno('Clear', 'Are you sure?')
    if question == 1:
        weight_enter.delete(0, END)
        height_enter.delete(0, END)
    elif question == 0:
        pass


window.title('BMI Calculator')

Title = LabelFrame(window, text='BMI CALCULATOR')

Weight = Label(Title, text='Weight :')
Height = Label(Title, text='Height :')

weight_enter = Entry(Title)
height_enter = Entry(Title)

# bd = border bd=0 mean border equal to 0 aka border = None
button_frame = LabelFrame(Title, bd=0)

Clear = Button(button_frame, text='Clear', command=clear)
Result = Button(button_frame, text='Result', command=BMI)
Exit = Button(button_frame, text='Exit', command=lambda: window.quit())


Title.pack(expand=True)

Weight.grid(row=0, column=0)
weight_enter.grid(row=0, column=1)

Height.grid(row=1, column=0)
height_enter.grid(row=1, column=1)

button_frame.grid(row=2, column=0, columnspan=3)
Result.pack(side='left', ipadx=10)
Clear.pack(side='left', ipadx=10)
Exit.pack(side='left', ipadx=10)

window.mainloop()
