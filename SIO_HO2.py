import tkinter as web

window = web.Tk()
window.title("Sam's Profile")
window.geometry('600x600')
window.resizable(False,False)
window.configure(bg = "dark red", cursor = "coffee_mug")

label = web.Label(window, text = "Student Profile", font= ("times new roman", "50", "bold"),fg = "black", bg = "dark red", anchor = "center")
label.pack(padx = 5, pady = 5)
label = web.Label(window, text = "Name: Sam Sio", font = ("times new roman", "15"), fg = "black", bg = "dark red")
label.pack(padx = 5,anchor = "w")
label = web.Label(window, text = "Age: 20", font = ("times new roman", "15"), fg = "black", bg = "dark red")
label.pack(padx = 5,anchor = "w")
label = web.Label(window, text = "Course: BSIT", font = ("times new roman", "15"), fg = "black", bg = "dark red")
label.pack(padx = 5,anchor = "w")
label = web.Label(window, text = "Birthday: January 25, 2006", font = ("times new roman", "15"), fg = "black", bg = "dark red")
label.pack(padx = 5,anchor = "w")
label = web.Label(window, text = "Motto:", font = ("times new roman", "15"), fg = "black", bg = "dark red")
label.pack(padx = 5,anchor = "w")
label = web.Label(window, text = "Just do it", font = ("times new roman", "15"), fg = "black", bg = "dark red")
label.pack(padx = 20,anchor = "w")

window.mainloop()