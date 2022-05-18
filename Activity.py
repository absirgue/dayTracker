from CategoryDataHandler import CategoryDataHandler


class Activity:
    def __init__(self, name, time):
        self.categorizer = CategoryDataHandler()
        self.name = name
        self.time = time
        self.hour = time.split(",")[1].split(":")[0].strip()
        self.category = self.categorizer.categorize(self.name)

    def getCategory(self):
        return self.category

    def getHour(self):
        return self.hour

    def getName(self):
        return self.name

    def __str__(self):
        return self.name + " " + self.time
