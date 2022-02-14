from tkinter import * 
import tkinter as tk
from tkinter.ttk import *
import keyboard

root = tk.Tk()
root.title("ShinyKeyboard")
root.geometry('720x480')
root.resizable(False, False)

menu_bar = Menu(root)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='File', menu=file_menu)
menu_bar.add_cascade(label='Options', menu=file_menu)
menu_bar.add_cascade(label='Cheats', menu=file_menu)
menu_bar.add_cascade(label='Tools', menu=file_menu)
menu_bar.add_cascade(label='Help', menu=file_menu)
root.config(menu=menu_bar)

bg = PhotoImage(file = "Background_PKM.png")
canvas1 = Canvas( root, width = 720, height = 480, highlightthickness=0)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = bg, anchor = "nw")

button01 = PhotoImage(file="button01_disabled_PKM.png")
canvas1.create_image( 219, 150, image = button01, anchor = "nw")

button02 = PhotoImage(file="button02_disabled_PKM.png")
canvas1.create_image( 219, 222, image = button02, anchor = "nw")

button03 = PhotoImage(file="button03_disabled_PKM.png")
canvas1.create_image( 219, 294, image = button03, anchor = "nw")

Art = PhotoImage(file="ArtzinhaBonitinha_PKM.png")
canvas1.create_image( 56, 195, image = Art, anchor = "nw")

textbox = PhotoImage(file="textbox_PKM.png")
canvas1.create_image( 0, 396, image = textbox, anchor = "nw")

mainloop()
