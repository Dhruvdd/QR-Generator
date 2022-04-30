import pyqrcode
from tkinter import *
import tkinter.ttk as ttk
import PIL
from PIL import ImageTk
from PIL import Image

win = Tk()
win.title("QR Code Generator")
win.config(background="#131E23")


def generate(): #it will generate qr code
    file_name = input("Enter QR Code Name :  ")
    save_path = r"/Users/dhruvdasadia/Documents/Project/QR-Code-Generator/" #give path of location where you wanted to store the png
    text = entry1.get()
    qr = pyqrcode.create(text)
    name  = save_path +file_name + ".png"
    
    qr.png(name, scale = 10)
    image = Image.open(name)
    image = image.resize((400,400), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    win.imagelabel.config(image=image)
    win.imagelabel.photo = image

text = ttk.Label(win,text = "Enter Link or Text :  ")
text.grid(row=0,column=0,padx=0,pady=0)

entry1 = ttk.Entry(win,width=40)
entry1.grid(row=0,column=1,padx=3,pady=3)

button =ttk.Button(win,text ="Generate",command=generate)
button.grid(row=1,column=0,padx=3,pady=3,columnspan=3)

show_qr = ttk.Label(win,text = "QR code: ")
show_qr.grid(row=1,column=0,padx=3,pady=3)

win.imagelabel = ttk.Label(win,background ="#fed304")
win.imagelabel.grid(row=2,column=0,padx=3,pady=3,columnspan=3)

win.mainloop()