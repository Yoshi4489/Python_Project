from tkinter import *

root = Tk()
root.title('To-Do List Application')

task_list = []
def submit():
    task = todo_enter.get()
    if task:
        task_list.append(task)
        todo_enter.delete(0, END)
        results.config(text='\n'.join(task_list))

def delete():
    task = delete_entry.get()
    if task in task_list:
        task_list.remove(task)
        delete_entry.delete(0, END)
        results.config(text='\n'.join(task_list))
    else:
        error_label.config(text=f"{task} not found in task list")

To_do_label = Label(root, text='Enter your task')
To_do_label.pack()

todo_enter = Entry(root)
todo_enter.pack()

submit_btn = Button(root, text='Enter', command=submit)
submit_btn.pack()

show = Label(root, text='Tasks:')
show.pack()

results = Label(root, text='')
results.pack()

delete_label = Label(root, text='Delete task:')
delete_label.pack()

delete_entry = Entry(root)
delete_entry.pack()

delete_btn = Button(root, text='Delete', command=delete)
delete_btn.pack()

error_label = Label(root, text='')
error_label.pack()

root.mainloop()
