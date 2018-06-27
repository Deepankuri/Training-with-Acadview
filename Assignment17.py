#Question1
"""
First we will import the tkinter module. Then we wil use label keyword to display the desired text 
and the button keyword to create a button for exiting the window.
"""
from tkinter import *
import tkinter as tk
r = tk.Tk()
w = tk.Label(r, text="Hello World")
w.pack()
button = tk.Button(r, text= "Exit", width=10, height=1, command=r.destroy)
button.pack()
r.mainloop()

#Question2
"""
We'll create a function to callback so that we can print text.
"""
from tkinter import *
import tkinter as tk
r = tk.Tk()

#defining a function to call back
def calling_back():
	printing = tk.Label(r, text="Hello World")
	printing.pack()

button = tk.Button(r, text= "Print", width=10, height=1, command=calling_back)
button.pack()
button = tk.Button(r, text= "Exit", width=10, height=1, command=r.destroy)
button.pack()
r.mainloop()

#Question3
"""
We'll create a frame and a function to change the text
"""
import tkinter as tk
r = tk.Tk()

frame = Frame(r, height=200, width=100)
frame.pack()

w = tk.Label(frame, text="Hello World")
w.pack()

#defining function to change text
def change_text():
	w.configure(text="Hi, you just changed the text")

button = tk.Button(frame, text= "Click here to change the text", width=30, height=1, fg='green', command=change_text)
button.pack()
button = tk.Button(frame, text= "Exit", width=10, height=1, fg='red', command=r.destroy)
button.pack()
r.mainloop()

#Question4
"""
We use get and entry for user input and button to print it.
"""
from tkinter import *
import tkinter as tk
r = tk.Tk()
w = tk.Label(r, text="Hello World")
w.pack()

def get_text():
	string = e.get()
	print(string)

e = Entry(r)
e.pack()
e.focus_set()

button = tk.Button(r, text= "Click to print your text", width=50, height=1, command=get_text)
button.pack()

button = tk.Button(r, text= "Exit", width=10, height=1, command=r.destroy)
button.pack()
r.mainloop()