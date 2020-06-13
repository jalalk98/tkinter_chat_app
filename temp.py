from tkinter import *
from tkinter import ttk

window = Tk()


def callback(event):
    event.widget.config({"bg": "white"})
    # print(sv.get())


def clickme():
    s = entry1.get()
    if s == "":
        entry1.config({"bg": "red"})
        entry2.config({"bg": "red"})
        entry1.focus_set()
    else:
        print("Failure")


entry1 = Entry(window)
entry2 = Entry(window)
entry1.pack()
entry2.pack()

entry1.bind("<Key>",callback)
entry2.bind("<Key>",callback)


button = Button(window, text="Click", command=clickme)
button.pack()

window.mainloop()
