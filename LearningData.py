
import os.path

#
#
# Class to handle reading of learning data fro file
# and writing data to file (including merging of ratings)
#
# Because of the size of the data involved , we use sets instead of
# lists
#

filename="LearningData.csv"


class LearningData(object):

    
    def __init__(self):
        print("LearningData: initialising class to handle learning data")

        self.LearntData = {}
        self.LearntData["version"] = 1

        self.loadLearningData()
        
        #
        # routine to read in learning data from file
        # file format is "move data",score  
        # each line has one data element on it
        #
        #
        

    def loadLearningData(self):
        userhome = os.path.expanduser('~')
        csvfile= os.path.join(userhome, 'Desktop', filename)
        filehandle = open(csvfile, "r")
        self.totalEntries=0
        for line in filehandle:
            self.data = line.split(",")
            self.movedata=""
            for i in range (0,len(self.data)-1):
                self.movedata=self.movedata+self.data[i]
            # add item to list
            self.LearntData[self.data[0]] = int(self.data[1]) # self.data[len(self.data)-1]
            self.totalEntries=self.totalEntries+1

        filehandle.close()
        print("LearningData: Entries read in:",self.totalEntries)


    def saveLearningData(self):
        userhome = os.path.expanduser('~')
        csvfile= os.path.join(userhome, 'Desktop', filename)
        filehandle = open(csvfile, "w")
        for i,item in enumerate (self.LearntData):
            self.itemscore = self.getScorefromHash(item)
            print(item+","+str(self.itemscore),file=filehandle)

        #close file
        filehandle.close()
        print("LearningData: Entries saved in:",len(self.LearntData))
        
            
    def getScorefromHash(self,hashInHex):
        self.value=0  # default value is 0 - no reward
        try:
            self.value = self.LearntData[hashInHex]
        except KeyError:
            # Key is not present
            pass
        return self.value

    def updateLearningData(self,historicalMoves,totalMoves,peicesLeft):
        # calculate score to increase data by
        self.score = int(1+(100/totalMoves))*peicesLeft
        self.score = self.score+1
        print("Game score is:" + str(self.score))
        for i in range(0,len(historicalMoves)):
            self.currentMove = historicalMoves[i]
            self.existingScore = self.getScorefromHash(self.currentMove)
            
            #save updated hash
            self.LearntData[self.currentMove] = self.existingScore + self.score 
                    

#
# execute main game class
#
if __name__ == '__main__':
    a_learningData = LearningData();
    total = a_learningData.getScorefromHash("29ef79d8cb1b6735f66d1b95f41715a4")
    print(str(total))
