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
import LearningData as ld
import copy as cp

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

    def setupTestBoard(self):
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
        self.checkers = np.append(self.checkers,chck.checker("E1",chck.black));
        self.checkers = np.append(self.checkers,chck.checker("D4",chck.black));
        self.checkers = np.append(self.checkers,chck.checker("C5",chck.black));
        self.checkers = np.append(self.checkers,chck.checker("D8",chck.black));

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
        self.checkers = np.append(self.checkers,chck.checker("E5",chck.white));
        self.checkers = np.append(self.checkers,chck.checker("F6",chck.white));
        self.checkers = np.append(self.checkers,chck.checker("D6",chck.white));


        print ("Length:"+str(len(self.checkers)));
        return


    def getCheckerAt(self,position):
#        print("getCheckerAt:"+position)
        for i in range (0,len(self.checkers)):
            if ((self.checkers[i].getPosition()==position) and (self.checkers[i].isActive())):
                return i
        return -1

#
#  this class returns a lists of valid moves
#
#  moves are seperated by commas
#  e.g. A1-B2,A3-B2,A1-B4
# Note:  musttakeapiece is aflag whihc causes this to only return moves whihc invoice taking a piece
#

    def getValidMoves(self,colour):
        self.validMoves = []

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

                # are we a double peice ? if so lets check backwards..
                if self.checkers[i].ifDouble():
                    # backwards to the left
                    self.avaialbleMoves = self.getDoubleMoveToLeft(self.checkers[i].getPosition(),colour)
                    if len(self.avaialbleMoves) >0:
                        self.validMoves.append(self.avaialbleMoves)

                    # and to the right backwards
                    self.avaialbleMoves = self.getDoubleMoveToRight(self.checkers[i].getPosition(),colour)
                    if len(self.avaialbleMoves) >0:
                        self.validMoves.append(self.avaialbleMoves)
                        
        return self.validMoves



    def getMoveToLeft(self,currentPosition,colour):
        # are we against the edge ?
        if ((colour == chck.white) and (currentPosition[1]=="1")):
            return ""
        if ((colour == chck.black) and (currentPosition[1]=="8")):
            return ""

        # are we at the end of board, so return ?
        if ((colour == chck.white) and (currentPosition[0]=="A")):
            return ""
        if ((colour == chck.black) and (currentPosition[0]=="H")):
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
            return currentPosition+"-"+self.avaialbeMove

        # fall through.. there is a piece, can we take it?
        if (self.checkers[self.blockPiece].getColour() != colour):
            # make sure that we are not taking piece off board.
            if self.checkers[self.blockPiece].getPosition()[1]=="1":
                return ""
            if self.checkers[self.blockPiece].getPosition()[1]=="8":
                return ""
            if self.checkers[self.blockPiece].getPosition()[0]=="A":
                return ""
            if self.checkers[self.blockPiece].getPosition()[0]=="H":
                return ""  
            # so far so good, not on edge of board
            self.jumpPosition = self.getCoords(self.avaialbeMove,self.directionOfPiece);
            self.blockPiece = self.getCheckerAt(self.jumpPosition);

            if (self.blockPiece==-1):
#                print("GetMoveToLeft: take a peice found")
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

        # are we at the end of board, so return ?
        if ((colour == chck.white) and (currentPosition[0]=="A")):
            return ""
        if ((colour == chck.black) and (currentPosition[0]=="H")):
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
            # make sure that we are not taking piece off board.
            if self.checkers[self.blockPiece].getPosition()[1]=="1":
                return ""
            if self.checkers[self.blockPiece].getPosition()[1]=="8":
                return ""
            if self.checkers[self.blockPiece].getPosition()[0]=="A":
                return ""
            if self.checkers[self.blockPiece].getPosition()[0]=="H":
                return ""  
            # so far so good, not on edge of board
            self.jumpPosition = self.getCoords(self.avaialbeMove,self.directionOfPiece);
            self.blockPiece = self.getCheckerAt(self.jumpPosition);
            if (self.blockPiece==-1):
                # no piece in the way so return move
#                print("GetMoveToRight: take a peice found")
                return currentPosition+"-"+self.jumpPosition+"("+self.avaialbeMove+")"

        # fall though no move to the right , so return blank
        return ""
    
########################################################################################
#
#  Is the Piece a double piece ?  is so lets explore moves backwards
#  Note: this function does not get if a double, calling code must do that
#  this just returns what moves are avaiallbe.  These work in the exact same way
# as the getMoveToLeft and getMovetoRight,  but in opposite direction
#
#########################################################################################

    def getDoubleMoveToLeft(self,currentPosition,colour):
        # are we against the edge ?
        if ((colour == chck.white) and (currentPosition[1]=="8")):
            return ""
        if ((colour == chck.black) and (currentPosition[1]=="1")):
            return ""

        # are we at the end of board, so return ?
        if ((colour == chck.white) and (currentPosition[0]=="H")):
            return ""
        if ((colour == chck.black) and (currentPosition[0]=="A")):
            return ""       

        self.directionOfPiece=""
        self.avaialbeMove = ""
        if (colour == chck.white):
            self.directionOfPiece = "DL"
        else:
            self.directionOfPiece="UL"

        self.avaialbeMove = self.getCoords(currentPosition,self.directionOfPiece);

        # we assume we could now have hit walls
        if (self.avaialbeMove==""):
            print("Bug found in getDoubleMoveToLeft")
            return ""

        self.blockPiece = self.getCheckerAt(self.avaialbeMove);
        if (self.blockPiece==-1):
            # no piece in the way so return move
            return currentPosition+"-"+self.avaialbeMove

        # fall through.. there is a piece, can we take it?
        if (self.checkers[self.blockPiece].getColour() != colour):
            # make sure that we are not taking piece off board.
            if self.checkers[self.blockPiece].getPosition()[1]=="1":
                return ""
            if self.checkers[self.blockPiece].getPosition()[1]=="8":
                return ""
            if self.checkers[self.blockPiece].getPosition()[0]=="A":
                return ""
            if self.checkers[self.blockPiece].getPosition()[0]=="H":
                return ""  
            # so far so good, not on edge of board
            self.jumpPosition = self.getCoords(self.avaialbeMove,self.directionOfPiece);
            self.blockPiece = self.getCheckerAt(self.jumpPosition);

            if (self.blockPiece==-1):
#                print("GetMoveToLeft: take a peice found")
                # no piece in the way so return move
                return currentPosition+"-"+self.jumpPosition+"("+self.avaialbeMove+")"
        # fall though no move to the left , so return blank
        return ""

    def getDoubleMoveToRight(self,currentPosition,colour):
        self.directionOfPiece="";
        # are we against the edge ?
        if ((colour == chck.white) and (currentPosition[1]=="1")):
            return ""
        if ((colour == chck.black) and (currentPosition[1]=="8")):
            return ""

        # are we at the end of board, so return ?
        if ((colour == chck.white) and (currentPosition[0]=="H")):
            return ""
        if ((colour == chck.black) and (currentPosition[0]=="A")):
            return ""
        
        self.avaialbeMove = ""
        if (colour == chck.white):
            self.directionOfPiece = "DR"
        else:
            self.directionOfPiece="UR"

        self.avaialbeMove = self.getCoords(currentPosition,self.directionOfPiece);

        # we assume we could now have hit walls
        if (self.avaialbeMove==""):
            print("Bug found in getDoubleMoveToRight")
            return ""

        self.blockPiece = self.getCheckerAt(self.avaialbeMove);
        if (self.blockPiece==-1):
            # no piece in the way so return move
            return currentPosition+"-"+self.avaialbeMove

        # fall through.. there is a piece, can we take it?
        if (self.checkers[self.blockPiece].getColour() != colour):
            # make sure that we are not taking piece off board.
            if self.checkers[self.blockPiece].getPosition()[1]=="1":
                return ""
            if self.checkers[self.blockPiece].getPosition()[1]=="8":
                return ""
            if self.checkers[self.blockPiece].getPosition()[0]=="A":
                return ""
            if self.checkers[self.blockPiece].getPosition()[0]=="H":
                return ""            
            
            # so far so good, not on edge of board
            self.jumpPosition = self.getCoords(self.avaialbeMove,self.directionOfPiece);
            self.blockPiece = self.getCheckerAt(self.jumpPosition);
            if (self.blockPiece==-1):
                # no piece in the way so return move
#                print("GetMoveToRight: take a peice found")
                return currentPosition+"-"+self.jumpPosition+"("+self.avaialbeMove+")"

        # fall though no move to the right , so return blank
        return ""







########################################################################################
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

        # encode and return hash value as a number
        hash_object = hashlib.md5(str.encode(self.hashstring))
        return hash_object.hexdigest()
                


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

#        print("getfutureBoardHash : "+nextMove)
        # get what piece is moving
        self.pieceToMove = nextMove[:2]
        self.pieceNewLocation = nextMove[3:5]
        self.pieceIndex = self.getCheckerAt(self.pieceToMove)
#        print("getfutureBoardHash:index location of:"+self.pieceToMove+" = "+str(self.pieceIndex))

        # if there a piece we need to take ?
        if nextMove.find("(") != 0:
            self.pieceTaken = nextMove[6:8]
            self.pieceTakenIndex= self.getCheckerAt(self.pieceTaken)
     
        self.hashlist = np.empty(0,dtype=object);
        for i in range (0,len(self.checkers)):
            # is current check active
            if  self.checkers[i].isActive():
                self.currentchecker =cp.copy(self.checkers[i])
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
        # encode and return hash value as a number
        hash_object = hashlib.md5(str.encode(self.hashstring))
        return hash_object.hexdigest()


#################################################################
#
#   makes a move, and updates the pices of the board
#   note:  this does not redraw the board on the screen
#
################################################################
    def makeMove(self,nextMove):
        self.pieceTakenIndex= -1
        self.pieceIndex = -1
        
        # get what piece is moving
        self.pieceToMove = nextMove[:2]
        self.pieceNewLocation = nextMove[3:5]
        self.pieceIndex = self.getCheckerAt(self.pieceToMove)

        # if there a piece we need to take ?
        if nextMove.find("(") >0:
            self.pieceTaken = nextMove[6:8]
            self.pieceTakenIndex= self.getCheckerAt(self.pieceTaken)
            print("taking piece"+self.pieceTaken+" index: "+str(self.pieceTakenIndex))
            # take piece
            self.colourTaken = self.checkers[self.pieceTakenIndex].getColour()
            self.checkers[self.pieceTakenIndex].takePiece()
            # reduce number of pieces on baord 

            if self.colourTaken == chck.black:
                self.blackPiecesLeft = self.blackPiecesLeft -1

            else:
                self.whitePiecesLeft = self.whitePiecesLeft -1

            
        for i in range (0,len(self.checkers)):
            # is current check active
            if  self.checkers[i].isActive():
                # have we found the piece we want to move
                if i == self.pieceIndex:
                    self.checkers[i].move(self.pieceNewLocation)

                    # have we become a double ???????
                    if self.checkers[i].getColour() == chck.white:
                        if self.checkers[i].getPosition()[0]=="A":
                            self.checkers[i].makeDouble();
                    else:
                         if self.checkers[i].getPosition()[0]=="H":
                            self.checkers[i].makeDouble();                           



        
    def PlayComputervsComputerGame(self):
        # who starts first
        self.whosTurn = chck.white

        # setup board
        self.setupBoard()

        # number of turns taken in the game (i.e. number of times a player has taken a turn)
        # note:  This does not increase if a player gets a free move when taking a oppisiton
        # piece, e,g, take two or more pieces in one go
        self.gameTurns = 0
        # variable to allow us to keep tack of pieces taken
        self.pieceJustTaken = False

        # number of pieces left, we start with 12, when we get to zero we know we have a winner
        self.blackPiecesLeft = 12
        self.whitePiecesLeft = 12

        # are we still playing flag
        self.stillPlaying = True

        # Load into memory the learning data from file...
        #TODO:  This needs to be done at start... will get big....
        
        LearntData = ld.LearningData()
        self.avaialbleMoves = []

        # draw board - get cals
        GamePanelWindow = gp.window()


        # main game loop
        while self.stillPlaying:
 
            # draw board
            GamePanelWindow.drawSquares()
            for i in range(0,len(self.checkers)):
                if self.checkers[i].isActive():
                    GamePanelWindow.drawChecker(self.checkers[i].getPosition(),self.checkers[i].getColour(),self.checkers[i].ifDouble())
            GamePanelWindow.update()

            # show whose turn it is
            if self.whosTurn == chck.white:
                print("White turn!")
            else:
                print("Black turn!")
                
            # get valid moves for current player
            self.avaialbleMoves = self.getValidMoves(self.whosTurn)
            print(self.avaialbleMoves)
            if len(self.avaialbleMoves) == 0:
                self.stillPlaying = False
                print("no moves avaialble...exiting")

            # debugging - wait for under input
 #           self.dummy=input("Press enter")


            self.moveScores = []
            self.totalScores = 0
            for i in range(0,len(self.avaialbleMoves)):
                self.hashcodeforMove = self.getFutureBoardHash(self.avaialbleMoves[i])
                self.currentScore = LearntData.getScorefromHash(self.hashcodeforMove)
                self.moveScores.append(self.currentScore)
                self.totalScores = self.totalScores + self.currentScore

            # if we have no learnt data for any of the moves
            # (i.e. totalscore = 0), we pick a random move.
            # otherwise we chose the higest move, unless 10% chance (epislon)
            # we take a random move
            
            if (self.stillPlaying):
                if self.totalScores == 0:
                    j = np.random.choice(len(self.avaialbleMoves));
                    print("Random move as no learning data:"+self.avaialbleMoves[j])
                    self.makeMove(self.avaialbleMoves[j])
                else:
                    # totalscores does not equal zero, so we have some learning data
                    # so we have a 10% change of random move, otherwise we take the best move
                    p = np.random.random();
                    if p<0.1:  #10%
                        j = np.random.choice(len(self.avaialbleMoves));
                        print("Random move (10% chance):"+self.avaialbleMoves[j])
                        self.makeMove(self.avaialbleMoves[j])
                  
                    else:
                        # we take the best move 90% of time
                        j = np.argmax(self.moveScores);  # get best score index
                        print("Best move (90% chance):"+self.avaialbleMoves[j])

                        self.makeMove(self.avaialbleMoves[j])                 
                
            # increase counter for number of moves taken
            self.gameTurns=self.gameTurns+1

            #who's turn is now
            if self.whosTurn == chck.white:
                self.whosTurn = chck.black
            else:
                self.whosTurn = chck.white

            # end of game?
            if ((self.whitePiecesLeft ==0) or (self.blackPiecesLeft ==0)):
                self.stillPlaying = False
                print("end of game detected - no pieces left")

 # end of game ############
        # draw board
        GamePanelWindow.drawSquares()
        for i in range(0,len(self.checkers)):
            if self.checkers[i].isActive():
                GamePanelWindow.drawChecker(self.checkers[i].getPosition(),self.checkers[i].getColour(),self.checkers[i].ifDouble())
        GamePanelWindow.update()

        if self.whitePiecesLeft==0:
            print("Black wins!")
        else:
            print("white wins!")
                
            
            


# **********************************************************
#
#  main launcher for app
#
# **********************************************************

    def run(self):

        # play computer against computer
        self.PlayComputervsComputerGame()
        

        return
#
# execute main game class
#
if __name__ == '__main__':
    a_game = game();
    a_game.run();
