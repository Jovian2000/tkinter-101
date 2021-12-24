import tkinter

window = tkinter.Tk()
window.title("Hello")
window.geometry("100x100")

block1 = tkinter.Label(
    window, 
    font = ("Arial", 15),
    text = "Hello\n tkinter!",
    bg ="DarkOliveGreen4",
    fg ="snow"
)
block1.pack(
    ipadx = 10,
    ipady = 10,
    fill = "both",
    expand = True
)

block2 = tkinter.Label(
    window,
    bg = "maroon",
    fg = "snow"
)
block2.pack(
    ipadx = 10,
    ipady = 10,
    fill = "both",
    expand = True,
    side = "left"
)

block3 = tkinter.Label(
    window,
    bg ="SkyBlue4",
    fg ="snow"
)
block3.pack(
    ipadx = 10,
    ipady = 10,
    fill = "both",
    expand = True,
    side = "right"
)

window.mainloop()