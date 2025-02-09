from tkinter import *

root = Tk()

root.title("MyFrame")

root.geometry("400x400")

label = Label(root, text="Demonstration of Frame in Python", bg="yellow", fg="black", font="10")
label.pack(pady=10)

F = Frame(root, bd=5)
F.pack()

frameLabel = Label(F, text="Frame Label", bg="red", fg="white")
frameLabel.pack()

BottomFrame = Frame(root)
BottomFrame.pack(side=BOTTOM)

bottomLabel = Label(BottomFrame, text="Bottom Labe", bg="yellow", fg="red")
bottomLabel.pack()

root.mainloop()