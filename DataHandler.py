from abc import abstractmethod
import csv


class DataHandler:

    def __init__(self):
        pass

    @abstractmethod
    def getFileName(self):
        pass

    def writeARow(self, row):
        with open(self.getFileName(), 'a') as f:
            writer = csv.writer(f)
            writer.writerow(row)

    def loadData(self):
        try:
            with open(self.getFileName(), 'r') as file:
                data = file.readlines()
                return data
        except:
            print("Failure to read CSV " + self.getFileName())
            return []

    @abstractmethod
    def clearData(self):
        pass

    def clear(self):
        f = open(self.getFileName(), "w+")
        f.close()
        self.clearData()
