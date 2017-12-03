import tkinter as tk
from tkinter import *
import checker as chck


class window(object):
    
    def __init__(self):
        self.master = Tk()
        self.Letters ="ABCDEFGH"
        self.w = Canvas(self.master, width=600, height=600)
        self.w.pack()
        X = self.w.winfo_width()
        Y = self.w.winfo_height()
        
        self.BoardSize = 400


        print(X)
        print(Y)
        
        self.drawSquares()
        

            
    def GetCanvas(self):
        return self.w
    def GetBoardSize(self):
        return self.BoardSize

    def drawSquares(self):#Draw Squares

        YInterval =  self.BoardSize/8
        XInterval = self.BoardSize/8

        XStart = 0
        self.w.delete("all")
        self.w.create_rectangle(0,0,400,400,fill="white")

        for Column in range(8):
            for Row in range(8):
                if((Column % 2 != 0)and(Row%2 !=0)):
                    self.w.create_rectangle(XInterval*Row, YInterval*Column,(XInterval*Row)+XInterval, YInterval*Column+YInterval, fill="blue")
                    Xstart = 600/8
                if(Row % 2+Column%2 ==0):
                    self.w.create_rectangle(XInterval*Row, YInterval*Column,(XInterval*Row)+XInterval, YInterval*Column+YInterval, fill="blue")



    def reDrawSquare(self,CoordXY):#Clear A Square
        PosX = self.Letters.find(CoordXY[0])
        PosY=int(CoordXY[1])-1
        Interval = self.BoardSize/8
        self.w.create_rectangle(PosX*Interval,PosY*Interval,(PosX*Interval)+Interval,(PosY*Interval)+Interval, fill="blue")    

    
    def drawChecker(self,CoordXY,Colour,isDouble):
        if (Colour == chck.white):
            FillColour="white"
        else:
            FillColour="black" 
        PosX = self.Letters.find(CoordXY[0])
        PosY=int(CoordXY[1])-1
        Interval = self.BoardSize/8
        self.w.create_oval(PosX*Interval,PosY*Interval,(PosX*Interval)+Interval,(PosY*Interval)+Interval, fill=FillColour) 

        if isDouble==True:
            self.w.create_oval(PosX*Interval,PosY*Interval,(PosX*Interval)+(Interval/2),(PosY*Interval)+(Interval/2), fill="green") 
            
    def close(self):
        self.master.destroy()

    def update(self):
        self.master.update()

#End of class


