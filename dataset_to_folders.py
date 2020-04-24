import csv
import zipfile
from os import path, makedirs

class DatasetAnalyzer:
    """

    """
    def __init__(self, zipPath, csvPath, keyWords = [], output = 'output/'):
        self.zipPath = zipPath
        self.csvPath = csvPath
        self.keyWords = keyWords
        self.output = output

        print(f'File to analyze {self.zipPath}')


    def createFolder(self, newPath):
        if not path.exists(newPath):
            makedirs(newPath)


    def listGenerator(self, zipfile):
        pass

    
    def processing(self):
        """
        """
        with open(self.csvPath, newline='') as csvfile:
            listreader = csv.reader(csvfile, delimiter=' ', quotechar=',')
            archive = zipfile.ZipFile(self.zipPath, 'r')    #Open zip file

            for row in listreader:
                row = str(row[0]).split(',')
                print(row)
                imgdata = archive.extract('ISBI2016_ISIC_Part3_Training_Data/'+str(row[0])+'.jpg', self.output + str(row[1]))

    



        
zipPath = 'dataset/ISBI2016_ISIC_Part3_Training_Data.zip'
csvPath = 'dataset/ISBI2016_ISIC_Part3_Training_GroundTruth.csv'

zip1 = DatasetAnalyzer(zipPath, csvPath, ['benign', 'malignant'] )
zip1.processing()