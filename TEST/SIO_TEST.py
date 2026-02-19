import tkinter as testi

window = testi.Tk()
window.title("Testinggg......")
window.geometry("1080x2340")
window.resizable(False, False)
window.configure(bg = "purple", cursor = "arrow")

label = testi.Label(window, text = "Image testing", font = ("times new roman", "20", "bold"), fg = "black", bg = "purple")
label.pack(pady = 10)

frame = testi.Frame(window, bg = "purple")
frame.pack()

img = testi.PhotoImage(file = "TEST/Cat.png")
img = img.subsample(15,15)
img_lable = testi.Label(frame, image = img, text = "Cute Cat",compound = "top")
img_lable.pack(pady = 10)

label3 = testi.Label(frame, text = "Username", font = ("times new roman", "20", "bold"), fg = "black", bg = "purple")
label3.pack(pady = 10)

username_test = testi.Entry(frame)
username_test.pack()

def test_show():
    username = username_test.get()
    label2 = testi.Label(window, text = "Button Clicked", font = ("times new roman", "20", "bold"), fg = "black", bg = "purple")
    label2.pack()
    label ["text"] = f"Hello,{username} You Clicked My Button"

button = testi.Button(window, text = "Submit",command = test_show, relief = "sunken", activebackground = "dark green", activeforeground = "purple")
button.pack()

window.mainloop()