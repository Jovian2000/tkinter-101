import tkinter as tk

root = tk.Tk()
root.title("Clicker")
root.geometry("200x200")
root.configure(bg = "grey")
count = 0

def colourChanges():
    global count
    if count > 0:
        root.configure(bg = "green")
    elif count < 0:
        root.configure(bg = "red")
    else:
        root.configure(bg = "grey")

def Up():
    global count
    count += 1
    countLabel.configure(text = count)
    colourChanges()

def down():
    global count
    count -= 1
    countLabel.configure(text = count)
    colourChanges()

buttonUp = tk.Button(
    root,
    command = Up,
    text = "Up"    
)
buttonUp.pack(
    ipadx = 55,  
    side = "top",
    expand = True
)

countLabel = tk.Label(
    root,
    text = count    
)
countLabel.pack(
    ipadx = 60,
    expand = True
)

buttonDown = tk.Button(
    root,
    command = down,
    text = "Down"
)
buttonDown.pack(
    ipadx = 45, 
    side = "bottom",
    expand = True
)

root.mainloop()