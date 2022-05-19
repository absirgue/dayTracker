import csv
from DataHandler import DataHandler
from datetime import datetime


class DayDataHandler(DataHandler):

    fileName = "dayRecords.csv"

    def __init__(self):
        DataHandler.__init__(self)
        self.data = []
        with open(self.fileName, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                tempList = []
                tempList.append(row[0])
                tempList.append(row[1])
                self.data.append(tempList)

    def getFileName(self):
        return self.fileName

    def record(self, event):
        now = datetime.now()
        currentTime = now.strftime("%m/%d/%Y, %H:%M:%S")
        self.lastTimeStamp = currentTime

        csvRow = [currentTime, event]
        self.data.append(csvRow)
        self.writeARow(csvRow)

    def getLastRow(self):
        if len(self.data) > 0:
            return self.data[-1]
        else:
            return []

    def documentIsEmpty(self):
        return len(self.data) == 0

    def getFirstTimeStamp(self):
        if self.documentIsEmpty():
            return ""
        else:
            return self.data[0][0]

    def clearData(self):
        self.data = []

    def getData(self):
        return self.data
