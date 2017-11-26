import tkinter as tk
from tkinter import *


class window():
    def __init__(self):
        master = Tk()
        self.Letters ="ABCDEFGH"
        self.w = Canvas(master, width=600, height=600)
        self.w.pack()
        X = self.w.winfo_width()
        Y = self.w.winfo_height()
        print(X)
        print(Y)
        
        window.drawSquares(self.w)
        

            
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



    def reDrawSquare(self,CoordX,CoordY,Colour,w):#Clear A Square
        
        PosX = self.Letters.find(CoordX)
        PosY = CoordY-1
        Interval = 600/8
        w.create_rectangle(PosX*Interval,PosY*Interval,(PosX*Interval)+Interval,(PosY*Interval)+Interval, fill=Colour)    

    
    def drawChecker(self,CoordX,CoordY,Colour,w):
        PosX = self.Letters.find(CoordX)
        PosY=CoordY-1
        Interval = 600/8
        w.create_oval(PosX*Interval,PosY*Interval,(PosX*Interval)+Interval,(PosY*Interval)+Interval, fill=Colour) 



#End of class

Window = window()
Canvas = Window.GetCanvas()
Window.reDrawSquare("A",6,"red",Canvas)
Window.drawChecker("A",6,"grey",Canvas)
Window.drawChecker("F",5,"black",Canvas)
Window.drawChecker("D",1,"grey",Canvas)

