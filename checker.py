
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

    def isDouble(self):
        return self.isDouble;


