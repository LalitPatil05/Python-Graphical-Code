import tkinter 
window = tkinter.Tk() # build / create the Frame
window.geometry("400x400") # ising this set the Size of the frame
window.title("GUI") # set the Title
label = tkinter.Label(window,text="Welcome to Tkinter.!").pack() # add the Label Component

window.mainloop() # final method to Intitialize the all