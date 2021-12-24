import tkinter
import time

def timeUpdate():
    firstnumbers = tkinter.StringVar(value=time.strftime('%H:%M:%S'))
    clock.set(firstnumbers)
    label.configure(textvariable=firstnumbers)
    root.after(200, timeUpdate)
    
root = tkinter.Tk()
root.title("Clock")
clock = tkinter.StringVar(value=time.strftime('%H:%M:%S'))

label = tkinter.Label(root,
    font = ("Modern", 200),
    bg = "black",
    fg = "red"
    )
label.configure(textvariable=clock)
label.pack(
    ipadx = 10,
    ipady = 10,
    fill = "both",
    expand = True
)

timeUpdate()

root.mainloop()
