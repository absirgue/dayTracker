from CategoryDataHandler import CategoryDataHandler


class Analyzer:

    def __init__(self, dayDataHandler, reportDate):
        self.date = reportDate
        self.data = dayDataHandler.getData()
        self.categoryToTimeMapping = {}
        self.categoryDecompositionMapping = {}
        self.hourDecompositionMapping = {}
        self.totalTime = 0

    def analyze(self, numberOfSecondsPerUnitsOfTime):
        self.totalTime = numberOfSecondsPerUnitsOfTime * len(self.data) / 60
        categorizer = CategoryDataHandler()
        print("self.data")
        print(self.data)
        for activity in self.data:
            category = categorizer.categorize(activity[1])
            if category in self.categoryToTimeMapping:
                self.categoryToTimeMapping[category] += 1
            else:
                self.categoryToTimeMapping[category] = 1

            self.recordActivityInCategoryDecomposition(category, activity[1])
            self.recordActivityinHourDecomposition(category, activity[0])
        self.calculatePercentages()
        self.produceTxt()

    def recordActivityInCategoryDecomposition(self, category, activity):
        if category in self.categoryDecompositionMapping:
            if activity in self.categoryDecompositionMapping[category]:
                self.categoryDecompositionMapping[category][activity] += 1
            else:
                print(self.categoryToTimeMapping)
                self.categoryToTimeMapping[category][activity] = 1
        else:
            self.categoryDecompositionMapping[category] = {}
            self.categoryDecompositionMapping[category][activity] = 1

    def recordActivityinHourDecomposition(self, category, time):
        hour = int(time.split(",")[1].split(":")[0].strip())
        if hour in self.hourDecompositionMapping:
            if category in self.hourDecompositionMapping[hour]:
                self.categoryDecompositionMapping[hour][category] += 1
            else:
                self.categoryDecompositionMapping[hour][category] = 1
        else:
            self.categoryDecompositionMapping[hour] = {}
            self.categoryDecompositionMapping[hour][category] = 1

    def calculatePercentages(self):
        totalTime = 0
        for category in self.categoryToTimeMapping:
            totalTime += self.categoryToTimeMapping[category]

        for category in self.categoryToTimeMapping:
            self.categoryToTimeMapping[category] = self.categoryToTimeMapping[category]/totalTime * 100

        for category in self.categoryDecompositionMapping:
            categoryTotalTime = 0
            for activity in self.categoryDecompositionMapping[category]:
                categoryTotalTime += self.categoryDecompositionMapping[category][activity]
            for activity in self.categoryDecompositionMapping[category]:
                self.categoryDecompositionMapping[category][activity] = self.categoryDecompositionMapping[
                    category][activity] / categoryTotalTime * 100

        for hour in self.hourDecompositionMapping:
            hourTotalTime = 0
            for category in self.hourDecompositionMapping[hour]:
                hourTotalTime += self.hourDecompositionMapping[hour][category]
            for category in self.hourDecompositionMapping[hour]:
                self.hourDecompositionMapping[hour][category] = self.hourDecompositionMapping[hour][category] / \
                    categoryTotalTime * 100

    def produceTxt(self):
        with open("[REPORT] " + self.date + ".txt", 'w') as f:
            f.write("Report" + "\n")
            f.write("" + "\n")
            f.write("General Analysis" + "\n")
            for category in self.categoryToTimeMapping:
                f.write("      - " + category + ": " +
                        str(self.categoryToTimeMapping[category]) + "%" + "\n")

            f.write("" + "\n")
            f.write("By Category Decomposition" + "\n")
            for category in self.categoryDecompositionMapping:
                f.write("      - " + str(category) + "\n")
                for activity in self.categoryDecompositionMapping[category]:
                    f.write("              + " + activity + ": " +
                            str(self.categoryToTimeMapping[category]) + "%" + "\n")

            f.write("" + "\n")
            f.write("By Hour Decomposition" + "\n")
            for hour in self.hourDecompositionMapping:
                f.write("      - " + str(hour) + "h" + "\n")
                for category in self.hourDecompositionMapping[hour]:
                    f.write("              + " + category + ": " +
                            str(self.hourDecompositionMapping[hour]) + "%" + "\n")
