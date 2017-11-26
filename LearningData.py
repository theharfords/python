
import csv


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

        #
        # routine to read in learning data from file
        # file format is "move data",score  
        # each line has one data element on it
        #
        #

    def loadLearningData(self):
        print("Hello")
        with open(filename, newline='') as csvfile:
            filereader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in filereader:
            print(', '.join(row))
        
        



# **********************************************************
#
#  main launcher for app
#
# **********************************************************

    def run(self):
        self.loadLearningData()
        return
#
# execute main game class
#
if __name__ == '__main__':
    a_learningData = LearningData();
    a_learningData.run();
