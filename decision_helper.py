from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.title('Decision Helper')
root.iconbitmap('c:/Users/user/MediaPipe Work shop/Image/Cat.jpeg')

def submit():
    question_enter.delete(0, END)
    yes = ['Yes', 'Just Do It!!!',  'Absolutely Yes', 'Actually', 'Of Course', 'Sure', 'Why Not!!!']
    no = ['No', 'Never',  'Actually no', 'Absolutely No']
    maybe = ['Maybe', 'Up To You', 'I don\'t know', 'None of my business']
    ans_list = [yes, no, maybe]
    pick_ans = random.choice(ans_list)
    last_ans = random.choice(pick_ans)
    messagebox.showwarning('Time Count', 5)
    messagebox.showwarning('Time Count', 4)
    messagebox.showwarning('Time Count', 3)
    messagebox.showwarning('Time Count', 2)
    messagebox.showwarning('Time Count', 1)
    messagebox.showinfo('Decision Helper', last_ans)


help_decision = Label(root, text='Let Us Help You!')
help_decision.grid(row=0, column=0, columnspan=3)

question = Label(root, text='Enter Your Question : ')
question.grid(row=1, column=0)

question_enter = Entry(root)
question_enter.grid(row=1, column=1, columnspan=2)

submit_button = Button(root, text='Submit Your Answer', command=submit)
submit_button.grid(row=2, column=0, ipadx=70, columnspan=2)

root.mainloop()
