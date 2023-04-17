from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('Grade Calculator')
window.geometry('400x200')
window.resizable(False, False)

# Create Function
def score_calculate():
    score = score_entry.get()
    try:
        score = int(score)
    except ValueError:
        messagebox.showerror('Error', 'คะแนนเป็นได้แค่ตัวเลข 1-100')
    score = int(score)
    if 0 <= score <= 49:
        messagebox.showinfo('คะแนน', 'คุณได้เกรด F')
    elif 49 < score <= 59:
        messagebox.showinfo('คะแนน', 'คุณได้เกรด D')
    elif 59 < score <= 69:
        messagebox.showinfo('คะแนน', 'คุณได้เกรด C')
    elif 69 < score <= 79:
        messagebox.showinfo('คะแนน', 'คุณได้เกรด B')
    elif 79 < score <= 100:
        messagebox.showinfo('คะแนน', 'คุณได้เกรด A')
    else:
        messagebox.showerror('Error', 'คะแนนเป็นได้แค่ตัวเลข 1-100')
    score_entry.delete(0, END)


# Create Frame
main_frame = LabelFrame(window, text='แอฟเช็คเกรด', padx=120, pady=60)
main_frame.pack(anchor='center')

# Create Label 
myLabel = Label(main_frame, text='กรุณากรอกคะแนนของคุณ 1-100')

# Create Entry
score_entry = Entry(main_frame, width=24)

# Create Button
submit_button = Button(main_frame, text='ยืนยัน', width=20, command=score_calculate)

# Create Grid
myLabel.grid(row=0, column=0)
score_entry.grid(row=1, column=0)
submit_button.grid(row=2, column=0)

window.mainloop()
