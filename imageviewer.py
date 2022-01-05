from tkinter import *
from PIL import ImageTk,Image
window=Tk()
window.title("Photo Viewer")
window.resizable(0, 0)

frame=Frame(window, width=600, height=500, bg='white', relief=GROOVE, bd=2)
frame.pack(padx=10, pady=10)
img1 = Image.open('image/img1.png')
img1.thumbnail((550, 450))
img2 = Image.open('image/img2.png')
img2.thumbnail((550, 450))
img3 = Image.open('image/img3.png')
img3.thumbnail((550, 450))
img4 = Image.open('image/img4.png')
img4.thumbnail((550, 450))

image1 = ImageTk.PhotoImage(img1)
image2 = ImageTk.PhotoImage(img2)
image3 = ImageTk.PhotoImage(img3)
image4 = ImageTk.PhotoImage(img4)

images = [image1, image2,image3, image4]

i = 0
image_label = Label(frame, image=images[i])
image_label.pack()

def previous():
    global i
    i = i - 1
    try:
        image_label.config(image=images[i])
    except:
        i = 0
        previous()
def next():
    global i
    i = i + 1
    try:
        image_label.config(image=images[i])
    except:
        i = -1
        next()

btn1 = Button(window, text="Previous",width=8, bd=5,bg='white', font=('cambria 15 bold'), relief=RAISED, command=previous)
btn1.pack(side=LEFT, padx=60, pady=5)
btn3 = Button(window, text="Exit", width=8,bd=5, bg='white', font=('cambria 15 bold'), relief=RAISED, command=window.destroy)
btn3.pack(side=LEFT, padx=60, pady=5)
btn2 = Button(window, text="Next", width=8, bd=5,bg='white', font=('cambria 15 bold'), relief=RAISED, command=next)
btn2.pack(side=LEFT, padx=60, pady=5)
window.mainloop()