
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
        print("Hello:"+os.getcwd()+"\\"+filename)

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
            self.LearntData[int(self.data[0],16)] = int(self.data[1]) # self.data[len(self.data)-1]
            self.totalEntries=self.totalEntries+1
            print(int(self.data[0],16))

        filehandle.close()
        print("Total entries read in:",self.totalEntries)
            
    def getScorefromHash(self,hashInHex):
        self.index = int(hashInHex,16)
        self.value=-1
        try:
            self.value = self.LearntData[self.index]
        except KeyError:
            # Key is not present
            pass
        return self.value
        



# **********************************************************
#
#  main launcher for app
#
# **********************************************************

    def run(self):
        return
#
# execute main game class
#
if __name__ == '__main__':
    a_learningData = LearningData();
    a_learningData.run();
    total = a_learningData.getScorefromHash("29ef79d8cb1b6735f66d1b95f41715a4")
    print(str(total))
