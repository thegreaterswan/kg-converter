from tkinter import *

window = Tk() #opens window and everything goes between this and the window.mainloop()

def kg_to_others():
    grams=1000*float(kg_in.get())
    pounds = 2.20462*float(kg_in.get())
    ounces = 35.274 * float(kg_in.get())
    tgrams.insert(END, grams)
    tpounds.insert(END, pounds)
    tounces.insert(END, ounces) 

b1 = Button(window, text="Convert", command=kg_to_others) #command is the fucntion that the button activates
b1.grid(row=0, column=2)

e1 = Label(window, text="Input Kg")
e1.grid(row=0, column=0)

kg_in_value = StringVar() 
kg_in = Entry(window, textvariable=kg_in_value) 
kg_in.grid(row=0, column=1)

tgrams = Text(window, height=1, width=20) #creates a text box for input, need to set the dimensional parameters
tgrams.grid(row=1, column=0)

tpounds = Text(window,height = 1, width = 20)
tpounds.grid(row=1, column = 1)

tounces = Text(window, height=1, width=20)
tounces.grid(row=1, column = 2)
