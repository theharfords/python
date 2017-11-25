import tkinter as tk
from tkinter import *


class window():
    def __init__(self):   #Sets Up
        master = Tk()

        w = Canvas(master, width=600, height=600)
        w.pack()
        X = w.winfo_width()
        Y = w.winfo_height()
        print(X)
        print(Y)

        window.drawSquares(w)
        
        mainloop()
    def GetCanvas(self):
        return self.w
    def drawSquares(W):#Draw Squares

        
        YInterval = 600/8
        XInterval = 600/8
        XStart = 0
        for Column in range(8):
            for Row in range(8):
                if((Column % 2 != 0)and(Row%2 !=0)):
                    W.create_rectangle(XInterval*Row, YInterval*Column,(XInterval*Row)+XInterval, YInterval*Column+YInterval, fill="blue")
                    Xstart = 600/8
                if(Row % 2+Column%2 ==0):
                    W.create_rectangle(XInterval*Row, YInterval*Column,(XInterval*Row)+XInterval, YInterval*Column+YInterval, fill="blue")



    def reDrawSquare(Coord,Colour,W):#Clear A Square
        Letters ="ABCDEFGH"
        PosX = Letters.find(Coord[0])
        PosY = int(Coord[1])
        Interval = 600/8
        W.create_rectangle(PosX*Interval,PosY*Interval,(PosX*Interval)+Interval, (PosX*Interval)+Interval, fill=Colour)    




        
Window = window()
Window.drawSquares()
Window.redrawSquare("A6","red",Window.GetCanvas())

