from tkinter import *
from tkinter import ttk

class GeoguessMain:

    def __init__(self, root):

        root.title("Geoguess 0.1")
        root.geometry('600x600')

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
       
        self.key = StringVar()
        key_entry = ttk.Entry(mainframe, width=7, textvariable=self.key)
        key_entry.grid(column=1, row=1, sticky=(W, E))
        
        ttk.Label(mainframe, textvariable=self.key).grid(column=2, row=2, sticky=(W, E))
        ttk.Button(mainframe, text="OK", command=self.key).grid(column=3, row=3, sticky=W)

        ttk.Label(mainframe, text="Введите ключ: ").grid(column=3, row=1, sticky=W)
        

root = Tk()
GeoguessMain(root)
root.mainloop()

"""

def key_checker():
    if 

"""