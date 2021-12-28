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