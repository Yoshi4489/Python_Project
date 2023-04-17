from tkinter import *
import requests

root = Tk()
root.title('URL Teller')

def onclick():
    url = url_input.get()
    response = requests.get(url)
    responses = response.text
    info_label.config(root, text='Your Website Info : ' + responses)
    url_input.delete(0, END)
    

# Create Label and Entry
myLabel = Label(root, text='Enter Your Website URL')
myLabel.pack()
url_input = Entry(root, width=30)
url_input.pack()
btn = Button(root, text='Enter', command=onclick)
btn.pack()
info_label = Label(root, text='Your Website Info : ')
info_label.pack()

root.mainloop()
