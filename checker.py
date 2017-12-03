
black = 1
white = 0

class checker(object):

    #
    #  class for each checker on the board
    #
    #


    def __init__(self,position,colour):
        self.position = position
        self.colour = colour
        self.onBoard = True
        self.isDouble = False

    def move(self,newPosition):
        self.position = newPosition;

    def getPosition(self):
        return self.position;

    def getColour(self):
        return self.colour;

    def isActive(self):
        return self.onBoard;

    def ifDouble(self):
        return self.isDouble;

    def takePiece(self):
        self.onBoard = False

    def makeDouble(self):
#        print("Congrats piece:"+self.position+" is now a double")
        self.isDouble = True


    # serialisation used for creating a hash of the board
    def serialisation(self):
        if self.onBoard == False:
            return ""
        self.text = self.position;
        if self.colour == black:
            self.text = self.text + "B"
        else:
            self.text = self.text + "W"
                
        if self.isDouble == True:
            self.text = self.text + "Q"
        else:
            self.text = self.text + "S"

        return self.text

