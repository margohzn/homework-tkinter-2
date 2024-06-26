from tkinter import * 
#from tkinter.ttk import * 

window = Tk()
window.geometry("500x600")
window.config(background = "navy")
window.title("Resteraunt Menu")

Email = Label(window, text = "Email: ", bg = "pink", fg = "black").place(x = 50, y = 50)
Email_input = Entry(window, width = 20).place(x = 130, y = 50)

Password = Label(window, text = "Password: ", bg = "pink", fg = "black").place(x = 50, y = 80)
Password_input = Entry(window , width = 20).place(x = 130, y = 80)

Food = Label(window, text = "What food would you like: chiken, pesto pasta, or nuggies", bg = "pink", fg = "black").place(x = 80, y = 150)
Food_answer = Entry(window, width = 20).place(x = 150, y = 190)

Drink = Label(window, text = "what drink would you like: water, cola or apple juice", bg = "pink", fg = "black").place(x = 95, y = 250)
Drink_answer = Entry(window, width = 20).place(x = 150, y = 290)

dessert = Label(window, text = "What dessert would you like: ice-cream, bread, or cake", bg = "pink", fg = "black").place(x = 80, y = 350)
Dessert_answer = Entry(window, width = 20).place(x = 150, y = 390)


button = Button(window, text = "Submit", bg = "navy").place(x = 210, y = 450)
#progress = Progressbar(window, orient = HORIZONTAL, length = 300, mode = "determinate")



window.mainloop()