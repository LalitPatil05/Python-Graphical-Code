from tkinter import *

window = Tk()

window.title("CheckBox Demo")

window.geometry("400x400")

label = Label(window, text="Demonstration of CheckButton", bd="5", fg="red", bg="white")
label.pack(pady="15")

document = Checkbutton(window, activebackground="red", bd=5, bg="white",
                    activeforeground="yellow", fg="green", text="Check me"   )

document.pack()

window.mainloop()