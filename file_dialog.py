from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title('Image viewer')

window.filename = filedialog.askopenfilename(initialdir='c:/Users/user/MediaPipe Work shop/Image', title='Select A file', filetypes=(("JPEG files", '.jpeg'), ('all files', '*.*')))
myIMG = ImageTk.PhotoImage(Image.open(window.filename))
myLAbel = Label(image=myIMG)
myLAbel.pack()

window.mainloop()
