from tkinter import *
from tkinter import ttk
from ttkbootstrap.constants import *
import ttkbootstrap as tb

class GeoguessMain:

    def __init__(self, root):

        root.title("Geoguess 0.1")
        root.geometry('1500x800')
        root.iconbitmap("gameico.png")

        KeyEnterLabel = tb.Label(text="Введите ключ:", font=("Halvetica", 18), bootstyle="LIGHT")
        KeyEnterLabel.pack(pady=40)

        KeyEntry = tb.Entry(root, width=25)
        KeyEntry.pack(pady=10)

        OkButton = ttk.Button(root, text="OK", bootstyle=SUCCESS, width=10)
        OkButton.pack(pady=40)
        
        
root = tb.Window(themename="superhero")
GeoguessMain(root)
root.mainloop()