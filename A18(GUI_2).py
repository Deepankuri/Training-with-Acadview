#Question1
"""
we will create a dictionary and then create scrollbar to
scroll through various values in it.
"""
from tkinter import *

root = Tk()

d = {"abc":"123", "def":"456", "ghi":"789", "jkl":"101112", "yetbf":"68713", "iksdyfgb":"97711","gfbueiytf":"36871", "kytv":"58716", "sudtcbife":"63781657","oduyv":"857", "duvbievtg":
'68713787', "isuhce":"34875"}

scrollbar = Scrollbar(root)
scrollbar.pack(side = LEFT, fill=BOTH)

l = Listbox(root, yscrollcommand = scrollbar.set)

for i in d:
	l.insert(END,i)
l.pack(side = LEFT)    
scrollbar.config(command = l.yview)

#Question2
"""
we tend to take input from the user to insert keys and values
into dictionary
"""
def func(x,y):
    d.update({x:int(y)})
    print(d)
    for i in d:
    	l.insert(END,i)

x = StringVar()
y = StringVar()


label_1 = Label(root, text="Enter the name", fg = 'blue')
label_2 = Label(root, text = "Enter the phone number", fg = 'blue')

entry_1 = Entry(root, textvariable=x)
entry_2 = Entry(root, textvariable=y)

label_1.pack()
entry_1.pack()
label_2.pack()
entry_2.pack()

b = Button(root, text = 'CLICK TO EXECUTE', command=lambda : func(x.get(), y.get()))
b.pack()
