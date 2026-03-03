#Label
#- Image
#- Button
#- Entry
#- Frame

#- checkbutton
#- Radio Button
#- Listbox

#- Scrollbar
#- Menu
#- TopLevel
import tkinter as testi

window = testi.Tk()
window.title("Testinggg......")
window.geometry("800x1422")
window.resizable(False, False)
window.configure(bg = "purple", cursor = "arrow")

menu = testi.Menu(window)#Menu
window ["menu"] = menu

file_drop = testi.Menu(menu, tearoff = 0)
file_drop.add_command (label = "New")
file_drop.add_command (label = "Open")
file_drop.add_command (label = "Exit")

menu.add_cascade(label = "File", menu = file_drop)

view_drop = testi.Menu(menu, tearoff = 1)
view_drop.add_command (label = "New")
view_drop.add_command (label = "Open")
view_drop.add_command (label = "Exit")

menu.add_cascade(label = "View", menu = view_drop)

label = testi.Label(window, text = "Image testing", font = ("times new roman", "20", "bold"), fg = "black", bg = "purple")
label.pack(pady = 5)

frame = testi.Frame(window, bg = "purple4")#frame
frame.pack(pady = 5)

img = testi.PhotoImage(file = "TEST/Cat.png")#image
img = img.subsample(15,15)
img_lable = testi.Label(frame, image = img, text = "Cute Cat",compound = "top")
img_lable.pack(pady = 5)

label3 = testi.Label(frame, text = "Username", font = ("times new roman", "20", "bold"), fg = "black", bg = "purple4")
label3.pack(pady = 5)

username_test = testi.Entry(frame)#entry
username_test.pack()

def test_show():
    username = username_test.get()#button
    label2 = testi.Label(window, text = "Button Clicked", font = ("times new roman", "15", "bold"), fg = "black", bg = "purple")
    label2.pack()
    label ["text"] = f"Hello,{username} You Clicked My Button"

    remember = check_val.get()#checkbutton
    if remember == 1:
        label4 = testi.Label(window, text = "You are remember", font = ("times new roman", "15", "bold"), fg = "black", bg = "purple")
        label4.pack()
    else: 
        label4 = testi.Label(window, text = "You are Not remember", font = ("times new roman", "15", "bold"), fg = "black", bg = "purple")
        label4.pack()

    gender = radio_val.get()#radiobutton
    if gender == 1:
        label5 = testi.Label(window, text = "You are Male", font = ("times new roman", "15", "bold"), fg = "black", bg = "purple")
        label5.pack()
    else:
        label5 = testi.Label(window, text = "You are Female", font = ("times new roman", "15", "bold"), fg = "black", bg = "purple")
        label5.pack()

    house = listbox.get(listbox.curselection())#listbox
    label6 = testi.Label(window, text = f"Your House is {house}", font = ("times new roman", "15", "bold"), fg = "black", bg = "purple")
    label6.pack()
        

radio_val = testi.IntVar()#radiobutton
female = testi.Radiobutton(frame, text = "Female", font = ("times new roman", "15", "bold"), fg = "black", bg = "purple4", variable = radio_val, value = 0)
female.pack()
male = testi.Radiobutton(frame, text = "Male", font = ("times new roman", "15", "bold"), fg = "black", bg = "purple4", variable = radio_val, value = 1)
male.pack()

listbox_lbl = testi.Label(frame, text = "Choose a House" , font = ("times new roman", "10", "bold"), fg = "black", bg = "purple4")#Listbox
listbox_lbl.pack()

scroll = testi.Scrollbar(frame)#Scrollbar
scroll.pack(side = "right", fill = "y")

listbox = testi.Listbox(frame,selectmode = "single", yscrollcommand = scroll.set)#List box and scrollbar
listbox.insert(0, "Python")
listbox.insert(1, "Java")
listbox.insert(2, "C++")
listbox.insert(3, "Perl")
listbox.insert(0, "Python")
listbox.insert(1, "Java")
listbox.insert(2, "C++")
listbox.insert(3, "Perl")
listbox.insert(0, "Python")
listbox.insert(1, "Java")
listbox.insert(2, "C++")
listbox.insert(3, "Perl")
listbox.insert(0, "Python")
listbox.insert(1, "Java")
listbox.insert(2, "C++")
listbox.insert(3, "Perl")
listbox.pack()

scroll["command"] = listbox.yview

check_val = testi.IntVar()#checkbutton
check_btn = testi.Checkbutton(frame, text = "Remember Me", font = ("times new roman", "15", "bold"), fg = "black", bg = "purple4", variable = check_val)
check_btn.pack()

button = testi.Button(window, text = "Submit",command = test_show, relief = "sunken", activebackground = "dark green", activeforeground = "purple")#button
button.pack()

popup = testi.Toplevel(window)#TopLevel
label = testi.Label(popup, text = "This is a TopLevel", font = ("times new roman", "20", "bold"), fg = "black", bg = "purple")
label.pack(pady = 5)
popup.transient(window)
popup.grab_set()

window.mainloop()

