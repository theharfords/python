


#
#
# Class to capture histroical moves, and give them a wieghting
# weighting is currently only based upon how many times the move is made
# but should also include how many peices were taken, or
# how many peices were lost?
#
# These last two pieces of functionality need to be added
#

class currentGameMoves(object):



    def __init__(self):
        print("currentGameMoves: initialising log of current gamemoves")
        self.historicalMoves = []

#
#  Adds a taken move to the list of moves already taken in the game
#  if a move has been used twice, the count is increased accordingly
#  e.g. The more times a move is taken, in a game which wins, by the biggest majority the bigger
#       the weighting this moves has.
#

    def addMove(self,moveTaken):
        try:
            b=self.historicalMoves.index(moveTaken)
        except ValueError:
            self.historicalMoves[moveTaken]=1
        else:
            self.historicalMoves[moveTaken]=self.historicalMoves[moveTaken]+1

        # have we taken a piece, if so increase by one or how many pieces were taken
        if "(" in moveTaken:
            self.historicalMoves[moveTaken]=self.historicalMoves[moveTaken]+1

        # if we take multiple pieces, these would be seperted by commas (future)
        self.historicalMoves[moveTaken]=self.historicalMoves[moveTaken]+moveTaken.count(",")

