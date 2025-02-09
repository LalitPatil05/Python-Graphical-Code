from tkinter import *

top = Tk()

top.geometry()
top.geometry("300x300")
top.title("CanvasDemo")
label = Label(top, text="Canvas Demo", fg="black", bg="red")
label.pack(pady="15")

cv = Canvas(top, bg= "yellow", height="200", width="200").pack()

top.mainloop()
