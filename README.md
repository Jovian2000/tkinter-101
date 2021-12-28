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
```
## F1.8.01.O5
Grabbelton
``` python
import tkinter as tk
from tkinter.messagebox import showinfo, showwarning
import random

items = ["telefoon", "laptop", "pc", "playstation", "xbox", "tv", "bluetooth speaker", "koptelefoon", "monitor", "tablet"]
GrabItem = ""

root = tk.Tk()
root.title("grabbelton")
root.configure(bg="black")
root.geometry("310x310")

button = tk.Button(
    root,
    command = lambda:[grab(), showinfo(
        title = "Gegrabbeld!",
        message = "Gefeliciteerd, je hebt een " + GrabItem + " gegrabbeld!" 
    )],
    text ="Grabbelen",
    font = ("Arial", 15),
    bg = "DarkOliveGreen4",
    fg = "snow2"
)
button.pack(
    padx = 100, 
    pady = 100,
)

label1 = tk.Label(
    root, 
    text = "Spullen in de grabbelton: " + str(len(items)),
    font = ("Arial", 14),
    bg = "grey5",
    fg = "white"
)
label1.pack(
    ipady = 20, 
    ipadx = 20,
    fill = "both",
    side = "bottom"
)

def grab():
    global GrabItem
    GrabItem = random.choice(items)
    items.remove(GrabItem)
    label1.configure(text = "Spullen in de grabbelton: " + str(len(items)))
    if len(items) == 0:
        button.configure(
            command = lambda: showwarning(
                title = "Klaar!",
                message = "U heeft alles uit de grabbelton gehaald!"
            )
        )

root.mainloop()
```
