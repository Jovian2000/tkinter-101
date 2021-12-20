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