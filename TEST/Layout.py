#Pack - top to bottom 
#Grid - rows and colomns (0,1,2) rows (0,1,2) colomns
#Place - x and y 
#Command - def 

import tkinter as sam

window = sam.Tk()
window.title("User Form")
window.geometry("350x200")
window.resizable(False, False)
window.configure(bg = "purple", cursor = "arrow")

row1 = sam.Label(window, text = "User Form", font = ("times new roman", "15", "bold"), fg = "black", bg = "purple")
row2 = sam.Label(window, text = "Username : ", font = ("times new roman", "15", "bold"), fg = "black", bg = "purple")
row21 = sam.Entry(window, font = ("times new roman", "15", "bold"), fg = "black", bg = "purple")
row3 = sam.Label(window, text = "Password :", font = ("times new roman", "15", "bold"), fg = "black", bg = "purple")
row31 = sam.Entry(window, font = ("times new roman", "15", "bold"), fg = "black", bg = "purple", show = "*")
row4 = sam.Button(window, text = "Submit", relief = "raised")

# row1.grid(row = 0, column = 0,columnspan = 4) #grid
# row2.grid(row = 1, column = 0, columnspan = 2)
# row21.grid(row = 1, column = 2, columnspan = 2)
# row3.grid(row = 2, column = 0, columnspan = 2)
# row31.grid(row = 2, column = 2, columnspan = 2)
# row4.grid(row = 3, column = 2, columnspan= 2)

row1.place(x=130, y=10) #place
row2.place(x=10, y=50)
row21.place(x=125, y=50)
row3.place(x=10, y=100)
row31.place(x=125, y=100)
row4.place(x=150, y=150)

#command
def color(event):
    row4 ["bg"] = "pink"

def ser(event):
    user = row21.get()
    print (user)

row4.bind("<Button-1>",color)
row21.bind("<Key>",ser)

window.mainloop()