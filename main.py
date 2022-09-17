from tkinter import *

window = Tk()

l1 = Label(window, text="Login Page")
l1.grid(row=0, column=0)

e1 = Entry(window)
e1.grid(row=1, column=0)

b1 = Button(window, text="Login as Employee")
b1.grid(row=2, column=0)

b2 = Button(window, text="Login as Employee")
b2.grid(row=3, column=0)
window.mainloop()
