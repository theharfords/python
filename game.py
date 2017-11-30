#
#
#
#
#
#
#

import numpy as np
import checker as chck
import GamePanel as gp
import hashlib

class game:

    def __init__(self):
        print("debug - game.py - init class");
        self.numberCheckers = 0;
        # max number of checkers on a board at anyone time = 24
        self.checkers = np.empty(0,dtype=object);
        return




    def setupBoard(self):
        # delete existing array if anything exists
        self.checkers = np.empty(0,dtype=object);
        # add black pieces
        self.checkers = np.append(self.checkers,chck.checker("A1",chck.black));
        self.checkers = np.append(self.checkers,chck.checker("A3",chck.black));
        self.checkers = np.append(self.checkers,chck.checker("A5",chck.black));
        self.checkers = np.append(self.checkers,chck.checker("A7",chck.black));
        self.checkers = np.append(self.checkers,chck.checker("B2",chck.black));
        self.checkers = np.append(self.checkers,chck.checker("B4",chck.black));
        self.checkers = np.append(self.checkers,chck.checker("B6",chck.black));
        self.checkers = np.append(self.checkers,chck.checker("B8",chck.black));
        self.checkers = np.append(self.checkers,chck.checker("C1",chck.black));
        self.checkers = np.append(self.checkers,chck.checker("C3",chck.black));
        self.checkers = np.append(self.checkers,chck.checker("C5",chck.black));
        self.checkers = np.append(self.checkers,chck.checker("C7",chck.black));

        # add white pieces
        self.checkers = np.append(self.checkers,chck.checker("H2",chck.white));
        self.checkers = np.append(self.checkers,chck.checker("H4",chck.white));
        self.checkers = np.append(self.checkers,chck.checker("H6",chck.white));
        self.checkers = np.append(self.checkers,chck.checker("H8",chck.white));
        self.checkers = np.append(self.checkers,chck.checker("G1",chck.white));
        self.checkers = np.append(self.checkers,chck.checker("G3",chck.white));
        self.checkers = np.append(self.checkers,chck.checker("G5",chck.white));
        self.checkers = np.append(self.checkers,chck.checker("G7",chck.white));
        self.checkers = np.append(self.checkers,chck.checker("F2",chck.white));
        self.checkers = np.append(self.checkers,chck.checker("F4",chck.white));
        self.checkers = np.append(self.checkers,chck.checker("F6",chck.white));
        self.checkers = np.append(self.checkers,chck.checker("F8",chck.white));


        print ("Length:"+str(len(self.checkers)));
        return

    def getCheckerAt(self,position):
        for i in range (1,len(self.checkers)):
            if ((self.checkers[i].getPosition()==position) and (self.checkers[i].isActive())):
                return i
        return -1

#
#  this class returns a lists of valid moves
#
#  moves are seperated by commas
#  e.g. A1-B2,A3-B2,A1-B4
#

    def getValidMoves(self,colour):
        self.validMoves = []
        if colour == chck.white:
            print("searching for moves for white")
        else:
            print("Searching for moves for black")

        for i in range (0,len(self.checkers)):
            # is current check right colour (we are looking for)
            if ((self.checkers[i].getColour()==colour) and (self.checkers[i].isActive())):
                # we have a match, so check avaialbe moves to the left
                self.avaialbleMoves = self.getMoveToLeft(self.checkers[i].getPosition(),colour)
                if len(self.avaialbleMoves) >0:
                    self.validMoves.append(self.avaialbleMoves)
                # and to the right
                self.avaialbleMoves = self.getMoveToRight(self.checkers[i].getPosition(),colour)
                if len(self.avaialbleMoves) >0:
                    self.validMoves.append(self.avaialbleMoves)

        return self.validMoves



    def getMoveToLeft(self,currentPosition,colour):
        # are we against the edge ?
        if ((colour == chck.white) and (currentPosition[1]=="1")):
            return ""
        if ((colour == chck.black) and (currentPosition[1]=="8")):
            return ""

        self.directionOfPiece=""
        self.avaialbeMove = ""
        if (colour == chck.white):
            self.directionOfPiece = "UL"
        else:
            self.directionOfPiece="DL"

        self.avaialbeMove = self.getCoords(currentPosition,self.directionOfPiece);

        # we assume we could now have hit walls
        if (self.avaialbeMove==""):
            print("Bug found in GetMoveToLeft")
            return ""

        self.blockPiece = self.getCheckerAt(self.avaialbeMove);
        if (self.blockPiece==-1):
            # no piece in the way so return move
            print("Found move: "+currentPosition+"-"+self.avaialbeMove)
            return currentPosition+"-"+self.avaialbeMove

        # fall through.. there is a piece, can we take it?
        if (self.checkers[self.blockPiece].getColour() != colour):
            self.jumpPosition = self.getCoords(self.avaialbeMove,self.directionOfPiece);
            self.blockPiece = self.getCheckerAt(self.avaialbeMove);
            if (self.blockPiece==-1):
                # no piece in the way so return move
                return currentPosition+"-"+self.jumpPosition+"("+self.avaialbeMove+")"
        # fall though no move to the left , so return blank
        return ""

    def getMoveToRight(self,currentPosition,colour):
        self.directionOfPiece="";
        # are we against the edge ?
        if ((colour == chck.white) and (currentPosition[1]=="8")):
            return ""
        if ((colour == chck.black) and (currentPosition[1]=="1")):
            return ""

        self.avaialbeMove = ""
        if (colour == chck.white):
            self.directionOfPiece = "UR"
        else:
            self.directionOfPiece="DR"

        self.avaialbeMove = self.getCoords(currentPosition,self.directionOfPiece);

        # we assume we could now have hit walls
        if (self.avaialbeMove==""):
            print("Bug found in GetMoveToRight")
            return ""

        self.blockPiece = self.getCheckerAt(self.avaialbeMove);
        if (self.blockPiece==-1):
            # no piece in the way so return move
            return currentPosition+"-"+self.avaialbeMove

        # fall through.. there is a piece, can we take it?
        if (self.checkers[self.blockPiece].getColour() != colour):
            self.jumpPosition = self.getCoords(self.avaialbeMove,self.directionOfPiece);
            self.blockPiece = self.getCheckerAt(self.avaialbeMove);
            if (self.blockPiece==-1):
                # no piece in the way so return move
                return currentPosition+"-"+self.jumpPosition+"("+self.avaialbeMove+")"

        # fall though no move to the right , so return blank
        return ""



#  getCoords function caulculates the coordinates of the square around the peice
# direction  two charactors
# charactor 0 = U = up board (C-B), D = Down Board,charactor 1 =  L = Left, R= Right
            # note:  left and right swap around depending if going down or up board
# if out of bounds - returns blank
#
    def getCoords(self,current,direction):
        self.newCoords = ""
        self.row = ord(current[0]);
        self.col = ord(current[1]);

        if (direction[0]=="U"):
            self.row=self.row-1
            if (direction[1]=="L"):
                self.col = self.col -1 # up left
            else:
                self.col = self.col +1 # up right

        if (direction[0]=="D"):
            self.row=self.row+1
            if (direction[1]=="L"):
                self.col = self.col +1 # down left
            else:
                self.col = self.col -1 # down right

        if ((self.col<49) or (self.col>56)):
            return ""
        if ((self.row<65) or (self.row>72)):
            return ""

        self.newCoords = chr(self.row) + chr(self.col)
        return self.newCoords



###############################################
#
#  returns a hash of the curent board setup
#
###############################################
    def getCurrentBoardHash(self):
        self.hashstring = ""
        self.hashlist = np.empty(0,dtype=object);
        for i in range (0,len(self.checkers)):
            # is current check right colour (we are looking for)
            if  self.checkers[i].isActive():
                self.hashlist=np.append(self.hashlist,self.checkers[i].serialisation());

        # sort the list
        self.hashlist = np.sort(self.hashlist)

        # crete hash
        for i in range (0,len(self.hashlist)):
                self.hashstring = self.hashstring +self.hashlist[i]+"."

        self.hash_object = hashlib.md5(str.encode(self.hashstring))
        print(str.encode(self.hashstring))
        return self.hash_object
                


###############################################
#
#  returns a hash of a future board setup given
#  a move
#
###############################################
    def getFutureBoardHash(self,nextMove):
        self.hashstring = ""
        self.pieceTakenIndex= -1
        self.pieceIndex = -1
        
        # get what piece is moving
        self.pieceToMove = nextMove[:2]
        self.pieceNewLocation = nextMove[3:5]
        self.pieceIndex = self.getCheckerAt(self.pieceToMove)

        # if there a piece we need to take ?
        if nextMove.index("(") != 0:
            self.pieceTaken = nextMove[6:8]
            self.pieceTakenIndex= self.getCheckerAt(self.pieceTaken)
     
        self.hashlist = np.empty(0,dtype=object);
        for i in range (0,len(self.checkers)):
            # is current check active
            if  self.checkers[i].isActive():
                self.currentchecker =self.checkers[i]
                # have we found the piece we want to move
                if i == self.pieceIndex:
                    self.currentchecker.move(self.pieceNewLocation)
                # are we the piece which was taken
                if i != self.pieceTakenIndex:
                    self.hashlist=np.append(self.hashlist,self.currentchecker.serialisation())

        # sort the list
        self.hashlist = np.sort(self.hashlist)
        
        # create hash
        for i in range (0,len(self.hashlist)):
                self.hashstring = self.hashstring +self.hashlist[i]+"."

        self.hash_object = hashlib.md5(str.encode(self.hashstring))
        print(str.encode(self.hashstring))
        return self.hash_object
                
        



# **********************************************************
#
#  main launcher for app
#
# **********************************************************

    def run(self):
        self.setupBoard();
        print("Piece :"+str(self.getCheckerAt("F8")));
        print(self.getValidMoves(chck.white))
        GamePanelWindow = gp.window()
        # draw checkers
        for i in range(0,len(self.checkers)):
            GamePanelWindow.drawChecker(self.checkers[i].getPosition(),self.checkers[i].getColour())
        GamePanelWindow.reDrawSquare("A1")
        print(self.getCurrentBoardHash())
        print(self.getFutureBoardHash("A1-B2(C3)"))
        return
#
# execute main game class
#
if __name__ == '__main__':
    a_game = game();
    a_game.run();
