import tkinter
from tkinter import PhotoImage
from tkinter import Canvas
from tkinter import Label
from tkinter import Frame
from tkinter import Button
from tkinter import RAISED
from tkinter import SUNKEN
from tkinter import LEFT
from tkinter import NW
from tkinter import TOP
from tkinter import Tk
root = tkinter.Tk()
root.geometry("655x333")
root.resizable(0,0)
f1 = Frame(root, bg="black", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")

f2 = Frame(root, borderwidth=8, bg="black", relief=SUNKEN)
f2.pack(side=TOP, fill="x",)

l1 = Label(f1, text="  INSTRUCTION TO USE  ")
l1.pack(pady=0)

l = Label(f1, text="Project Tkinter")
l.pack( pady=42)

l2 = Label(f2, text="CONVERSION GUI", font="Helvetica 16 bold", fg="black", bg = "grey",pady=22)
l2.pack()



canvas_w=400
canvas_h=400
can_widget=Canvas(root,width=canvas_w, height=canvas_h)
can_widget.pack(anchor=NW)

can_widget.create_rectangle(5, 0,15, 400,fill="grey")



b1=Button(root,text="annnnnn",font = " helvatica 12 bold",bg="black",fg="red",borderwidth=6, relief=RAISED)
b1.place(x=180,y=100,height=60,width=80)

root.mainloop()