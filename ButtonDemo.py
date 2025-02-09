import tkinter

window = tkinter.Tk()
window.geometry("400x400")

window.title("Button GUI")
label = tkinter.Label(window, text="Button Demo", bg="yellow", fg="black", bd="5")
label.pack(pady=20)
ButtonWidget = tkinter.Button(window,text="Click", bd=5)
ButtonWidget2 = tkinter.Button(window,text="Submit", bd=5)


ButtonWidget.pack(pady=15, padx=10)
ButtonWidget2.pack(pady=10, padx=10)

tkinter.mainloop()