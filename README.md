# tkinter-101
## F8.01.O1
Deze GUI inspireert mij het meest, want het is op windows. Ik ben daarmee ook het meest bekend bij.
Het ziet er ook gewoon makkelijk uit en de overzicht is ook duidelijk
## F8.01.O2
Explosief Venster Gebruik
``` python
import tkinter 

window = tkinter.Tk()
window.title("My first window")
window.geometry("50x50")
number = 100
colorList = ["white", "yellow", "orange", "red", "purple", "black",""]
colorChoice = 0
count = 6

def updateWindows():
    global number, colorChoice, count 
    window.geometry(str(number)+"x"+str(number))
    window.config(bg=colorList[colorChoice])
    number += 50    
    colorChoice += 1
    if count <= 0:
        window.destroy()
        print("BOOM!")
    else:
        print(count)
    count -= 1

for i in range(7):
    window.after(2000*i, updateWindows)



window.mainloop()
```
## F1.8.01.O3
Hello tkinter!
``` python
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
```
## F1.8.01.O4
Een klok
``` python
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
```