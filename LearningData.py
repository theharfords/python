
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
# https://1drv.ms/u/s!AnpUjYT6qxSdnfQkbeS_B3I1srYqFA


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
            self.LearntData[self.movedata] = 1 # self.data[len(self.data)-1]
            self.totalEntries=self.totalEntries+1

        filehandle.close()
        print("Total entries read in:",self.totalEntries)
            
        
        



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
