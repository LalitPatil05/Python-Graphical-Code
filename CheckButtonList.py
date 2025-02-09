from tkinter import *

root = Tk()

root.geometry("400x400")

root.title("Dashboard")

label = Label(root, text="Demonstration of Checkbutton", bd="5", bg="yellow",
              fg="red", font="100")

label.pack(pady="15")

Checkbutton1 = IntVar()
Checkbutton2 = IntVar()
Checkbutton3 = IntVar()


Button1 = Checkbutton(root, text="HomePage",variable=Checkbutton1, onvalue=1, offvalue=0, 
                 height=5, width=10)

Button2 = Checkbutton(root, text="About Us",variable=Checkbutton2,
                 onvalue=1, offvalue=0, height=5, width=10)

Button3 = Checkbutton(root, text="Contact",variable=Checkbutton3,
                 onvalue=1, offvalue=0, height=5, width=10)

Button1.pack(pady=10)
Button2.pack(pady=10)
Button3.pack(pady=10)


root.mainloop()