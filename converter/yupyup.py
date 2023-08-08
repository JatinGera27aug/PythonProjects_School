import tkinter
from PIL import ImageTk,Image
from tkinter import PhotoImage
from tkinter import Canvas
from tkinter import Label
from tkinter import Frame
from tkinter import Button
from tkinter import Tk
from tkinter import ttk
#from tkinter import*
def again():
    canva = Canvas(root,width=500,height=500,bg="black")
    canva.bind('<Button-1>',press)
    canva.place(x=0,y=0)
    #l1=Label(root,font
    l1=Label(root,text="Move your pointer...",font=" helvetica 13 bold ",fg="white",bg="black")#
    l1.place(x=160,y=180)
    l2=Label(root,text="  Left click and hold it still",font=" helvetica 11 bold ",fg="white",bg="black")
    l2.place(y=220,x=150)
    root.mainloop()

def press(event):
    print('Left click at x=%d,y=%d'%(event.x,event.y))
    l1.destroy()
    l2.destroy()
    canva.destroy()
     #print('left click at x=%d'%(event.x))
    #if event.x <= 27 and event.y <=70 :
    if (event.x >= 0 and event.x <= 30) and (event.y>=40 and event.y <=70):
        im = PhotoImage(file="rum.png")
        labeage = Label(root,image = im,height=500,width=500)
        labeage.place(x=0,y=0)
        b1 = Button(root,text="Do it Again",fg="black",bg="pink",font="helvetica 6 bold",borderwidth=0,command=again)
        b1.place(x=420,y=10)
        root.mainloop()
    if (event.x >= 250 and event.x <= 270) and (event.y>=60 and event.y <=80):
        
        im1 = PhotoImage(file="pp14.png")
        labeage = Label(root,image = im1,height=500,width=500)
        labeage.place(x=0,y=0)
        b1 = Button(root,text="Do it Again",fg="black",bg="pink",font="helvetica 6 bold",borderwidth=0,command=again)
        b1.place(x=420,y=10)
        root.mainloop()
    if (event.x <=230 and event.x >=218)  and (event.y >=30 and event.y <=40):
        
        im2 = PhotoImage(file="pp8.png")
        labeage = Label(root,image = im2,height=500,width=500)
        labeage.place(x=0,y=0)
        b1 = Button(root,text="Do it Again",fg="black",bg="pink",font="helvetica 6 bold",borderwidth=0,command=again)
        b1.place(x=420,y=10)
        root.mainloop()   
    if (event.x <=265 and event.x >=245)  and (event.y <=320 and event.y >=280):
        
        im3 = PhotoImage(file="pp7.png")
        labeage = Label(root,image = im3,height=500,width=500)
        labeage.place(x=0,y=0)
        b1 = Button(root,text="Do it Again",fg="black",bg="pink",font="helvetica 6 bold",borderwidth=0,command=again)
        b1.place(x=420,y=10)
        root.mainloop()   
    if (event.x <=500 and event.x >=480)  and (event.y >=45 and event.y <=65):
        
        im4 = PhotoImage(file="pp2.png")
        labeage = Label(root,image = im4,height=500,width=500)
        labeage.place(x=0,y=0)
        b1 = Button(root,text="Do it Again",fg="black",bg="pink",font="helvetica 6 bold",borderwidth=0,command=again)
        b1.place(x=420,y=10)   
        root.mainloop()   
    if (event.x <=45 and event.x >=15)  and (event.y >=235 and event.y <=265):
        
        im5 = PhotoImage(file="pp5.png")
        labeage = Label(root,image = im5,height=500,width=500)
        labeage.place(x=0,y=0)
        b1 = Button(root,text="Do it Again",fg="black",bg="pink",font="helvetica 6 bold",borderwidth=0,command=again)
        b1.place(x=420,y=10)
        root.mainloop()  
    if (event.x <=240 and event.x >=205)  and (event.y >=305 and event.y <=355):
        
        im6 = PhotoImage(file="pp4.png")
        labeage = Label(root,image = im6,height=500,width=500)
        labeage.place(x=0,y=0)
        b1 = Button(root,text="Do it Again",fg="black",bg="pink",font="helvetica 6 bold",borderwidth=0,command=again)
        b1.place(x=420,y=10)
        root.mainloop()  
    if (event.x <=25 and event.x >=0)  and (event.y >=0 and event.y <=20):
        
        im7 = PhotoImage(file="pp18.png")
        labeage = Label(root,image = im7,height=500,width=500)
        labeage.place(x=0,y=0)
        b1 = Button(root,text="Do it Again",fg="black",bg="pink",font="helvetica 6 bold",borderwidth=0,command=again)
        b1.place(x=420,y=10)
        root.mainloop()  
    if (event.x <=115 and event.x >=90)  and (event.y >=50 and event.y <=85):
        
        im7 = PhotoImage(file="pp12.png")
        labeage = Label(root,image = im7,height=500,width=500)
        labeage.place(x=0,y=0)
        b1 = Button(root,text="Do it Again",fg="black",bg="pink",font="helvetica 6 bold",borderwidth=0,command=again)
        b1.place(x=420,y=10)
        root.mainloop()  
    if (event.x <=160 and event.x >=120)  and (event.y >=305 and event.y <=370):
        
        im8 = PhotoImage(file="pp16.png")
        labeage = Label(root,image =im8 ,height=500,width=500)
        labeage.place(x=0,y=0)
        b1 = Button(root,text="Do it Again",fg="black",bg="pink",font="helvetica 6 bold",borderwidth=0,command=again)
        b1.place(x=420,y=10)
        root.mainloop()  
    # if (event.x <= and event.x >=)  and (event.y >= and event.y <=):
        
    #     im = PhotoImage(file=".png")
    #     labeage = Label(root,image = im,height=500,width=500)
    #     labeage.place(x=0,y=0)
    #     b1 = Button(root,text="Do it Again",fg="black",bg="pink",font="helvetica 6 bold",borderwidth=0,command=again)
    #     b1.place(x=420,y=10)
    #     root.mainloop()  
    else:
        
        print("jjj")

root=Tk()
root.geometry("500x500+120+120")
root.resizable(0,0)

canva = Canvas(root,width=500,height=500,bg="black")
canva.bind('<Button-1>',press)
canva.place(x=0,y=0)
l1=Label(root,text="Move your pointer...",font=" helvetica 13 bold ",fg="white",bg="black")#
l1.place(x=160,y=180)
l2=Label(root,text="  Left click and hold it still",font=" helvetica 11 bold ",fg="white",bg="black")
l2.place(y=220,x=150)
root.mainloop()




