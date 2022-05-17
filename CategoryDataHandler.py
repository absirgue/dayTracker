import csv
from DataHandler import DataHandler


class CategoryDataHandler(DataHandler):
    activityToCategory = {}
    categoryFilePath = "categories.csv"

    def __init__(self):
        with open(self.categoryFilePath, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                activity = row[0]
                category = row[1]
                self.activityToCategory[activity] = category
        print("hello there")
        print(self.activityToCategory)

    def clearData(self):
        pass

    def getFileName(self):
        return self.categoryFilePath

    def categorize(self, activity):
        print(activity)
        if activity in self.activityToCategory:
            return self.activityToCategory[activity]
        else:
            self.writeARow([activity, "Uncategorized"])
            return "Uncategorized"
