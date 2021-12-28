import tkinter
import time

def timeUpdate():
    clock = tkinter.StringVar(value=time.strftime('%H:%M:%S'))
    label.configure(textvariable=clock)
    root.after(50, timeUpdate)
    
root = tkinter.Tk()
root.title("Clock")

label = tkinter.Label(root,
    font = ("Modern", 200),
    bg = "black",
    fg = "red"
    )
label.pack(
    ipadx = 10,
    ipady = 10,
    fill = "both",
    expand = True
)

timeUpdate()

root.mainloop()
