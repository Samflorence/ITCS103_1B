import tkinter as sam

window = sam.Tk()
window.title("Simple Calculator Application")
window.geometry("265x200")
window.resizable(False, False)
window.configure(bg= "purple", cursor= "arrow")

frame = sam.Frame(window, bg= "white", width= 290, height= 25)
frame.place(x= 0, y= 0)

title = sam.Label(frame, text= "Simple Calculator", font= ("times new roman", "10"), bg= "white")
title.place(x= 80, y= 3)

number1 = sam.Label(window, text= "Enter 1st Number:", font= ("times new roman", "10"))
number1.place(x= 20, y= 30)

number1_entry = sam.Entry(window, font= ("times new roman", "10"))
number1_entry.place(x= 125, y= 30)

number2 = sam.Label(window, text= "Enter 2st Number:", font= ("times new roman", "10"))
number2.place(x= 20, y= 70)

number2_entry = sam.Entry(window, font= ("times new roman", "10"))
number2_entry.place(x= 125, y= 70)

def add():
    numbers1 = eval(number1_entry.get())
    numbers2 = eval(number2_entry.get())

    add = numbers1 + numbers2

    title ["text"] = f"The sum of {numbers1} + {numbers2} is {add}." 

add_btn = sam.Button(window, text= "ADD", relief= "raised", font= ("times new roman", "10"),command= add)
add_btn.place(x= 80, y= 100)

def sub():
    numbers1 = eval(number1_entry.get())
    numbers2 = eval(number2_entry.get())

    sub = numbers1 - numbers2

    title ["text"] = f"The subtraction of {numbers1} - {numbers2} is {sub}." 

subtract_btn = sam.Button(window, text= "SUBTRACT", relief= "raised", font= ("times new roman", "10"),command= sub)
subtract_btn.place(x= 150, y= 100)

def mul():
    numbers1 = eval(number1_entry.get())
    numbers2 = eval(number2_entry.get())

    mul = numbers1 * numbers2

    title ["text"] = f"The multiplication of {numbers1} * {numbers2} is {mul}." 

multiply_btn = sam.Button(window, text= "MULTIPLY", relief= "raised", font= ("times new roman", "10"),command= mul)
multiply_btn.place(x= 65, y= 130)

def div():
    numbers1 = eval(number1_entry.get())
    numbers2 = eval(number2_entry.get())

    div = numbers1 / numbers2

    title ["text"] = f"The division of {numbers1} / {numbers2} is {div}." 

division_btn = sam.Button(window, text= "DIVISION", relief= "raised", font= ("times new roman", "10"),command= div)
division_btn.place(x= 160, y= 130)

window.mainloop()