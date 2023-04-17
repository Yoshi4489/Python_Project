from tkinter import * 
from PIL import ImageTk, Image

root = Tk()
root.title('Image Slide')
image_1 = ImageTk.PhotoImage(Image.open('c:/Users/user/OneDrive/รูปภาพ/Saved Pictures/blender.jpg'))
image_2 = ImageTk.PhotoImage(Image.open('c:/HTML/Thumbnails/ijuhuih.webp'))
image_3 = ImageTk.PhotoImage(Image.open('c:/HTML/Thumbnails/idol.webp'))
image_4 = ImageTk.PhotoImage(Image.open('c:/HTML/Thumbnails/hq720.webp'))
image_5 = ImageTk.PhotoImage(Image.open('c:/HTML/Thumbnails/hqdefault.webp'))

image_list = [image_1, image_2, image_3, image_4, image_5]

status = Label(root, text='Image 1 of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E) # bd = border anchor = สมอไว้ทาง east(ล็อกไว้ที่ทิศ east) relief = style

my_label = Label(image=image_1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_next
    global button_back

    my_label.grid_forget() # ลบ grid เก่า
    my_label = Label(image=image_list[image_number-1])
    button_next = Button(text=">>", command=lambda: forward(image_number+1))
    button_back = Button(text='<<', command=lambda: back(image_number-1))
    status_img = Label(root, text='Image ' + str(image_number) + 'of' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

    if image_number == 5:
        button_next = Button(text='>>', state=DISABLED) # หยุดการทำงานของ command

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_next.grid(row=1, column=2)
    status_img.grid(row=2, column=0, columnspan=3, sticky=W + E)

def back(image_number):
    global my_label
    global button_next
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_next = Button(text=">>", command=lambda: forward(image_number+1))
    button_back = Button(text='<<', command=lambda: back(image_number-1))
    my_label = Label(image=image_list[image_number-1])
    status_labe = Label(root, text='Image ' + str(image_number) + 'of' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

    if image_number == 1:
        button_back  = Button(text="<<", state=DISABLED)
        button_next = Button(text=">>", command=lambda: forward(image_number+1))
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_next.grid(row=1, column=2)
    status_labe.grid(row=2, column=0, columnspan=3, sticky=W + E)



button_back = Button(text='<<', command=back, state=DISABLED)
button_exit = Button(text='Exit Program', command=root.quit)
button_next = Button(text='>>', command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_next.grid(row=1, column=2)
status.grid(row=2, column=0, columnspan=3,  sticky=W+E)  # ติดหนึบทิศwest to east

root.mainloop()
