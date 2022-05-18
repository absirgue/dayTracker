from Activity import Activity


class Analyzer:

    def __init__(self, dayDataHandler, reportDate):
        self.date = reportDate
        self.dayDataHandler = dayDataHandler
        self.categoryToTimeMapping = {}
        self.categoryDecompositionMapping = {}
        self.hourDecompositionMapping = {}
        self.totalTime = 0
        self.activityList = []
        self.lines = []

    def analyze(self, numberOfSecondsPerUnitsOfTime):
        self.totalTime = numberOfSecondsPerUnitsOfTime * \
            len(self.dayDataHandler.getData()) / 60
        self.recordActivities()
        self.produceAnalysis()
        self.produceTxt()

    def recordActivities(self):
        for activity in self.dayDataHandler.getData():
            self.activityList.append(Activity(activity[1], activity[0]))

    def produceAnalysis(self):
        self.produceGeneralAnalysis()
        self.produceHourlyAnalysis()
        self.produceCategoryAnalysis()

    def produceGeneralAnalysis(self):
        for activity in self.activityList:
            if activity.getCategory() in self.categoryToTimeMapping:
                self.categoryToTimeMapping[activity.getCategory()] += 1
            else:
                self.categoryToTimeMapping[activity.getCategory()] = 1

    def produceHourlyAnalysis(self):
        for activity in self.activityList:
            if activity.getHour() in self.hourDecompositionMapping:
                if activity.getCategory() in self.hourDecompositionMapping[activity.getHour()]:
                    self.hourDecompositionMapping[activity.getHour(
                    )][activity.getCategory()] += 1
                else:
                    self.hourDecompositionMapping[activity.getHour(
                    )][activity.getCategory()] = 1
            else:
                self.hourDecompositionMapping[activity.getHour()] = {}
                self.hourDecompositionMapping[activity.getHour(
                )][activity.getCategory()] = 1

    def produceCategoryAnalysis(self):
        for activity in self.activityList:
            if activity.getCategory() in self.categoryDecompositionMapping:
                if activity.getName() in self.categoryDecompositionMapping[activity.getCategory()]:
                    self.categoryDecompositionMapping[activity.getCategory(
                    )][activity.getName()] += 1
                else:
                    self.categoryDecompositionMapping[activity.getCategory(
                    )][activity.getName()] = 1
            else:
                self.categoryDecompositionMapping[activity.getCategory()] = {}
                self.categoryDecompositionMapping[activity.getCategory(
                )][activity.getName()] = 1

    def produceTxt(self):
        self.produceTxtHeader()
        self.produceTxtGeneralAnalysis()
        self.produceTxtCategoryAnalysis()
        self.produceTxtHourAnalysis()
        self.writeDocument()

    def produceTxtHeader(self):
        self.lines.append("Report" + "\n")
        self.lines.append("" + "\n")

    def produceTxtGeneralAnalysis(self):
        totalTime = 0
        for category in self.categoryToTimeMapping:
            totalTime += self.categoryToTimeMapping[category]

        self.lines.append("General Analysis" + "\n")
        for category in self.categoryToTimeMapping:
            self.lines.append("      - " + category + ": " +
                              str(self.categoryToTimeMapping[category]*100//totalTime) + "%")
            self.lines.append("\n")

    def produceTxtCategoryAnalysis(self):
        self.lines.append("Category Analysis" + "\n")

        print(self.categoryDecompositionMapping)
        for category in self.categoryDecompositionMapping:
            categoryTime = 0
            self.lines.append("      - " + category + ": " + "\n")
            for activity in self.categoryDecompositionMapping[category]:
                categoryTime += self.categoryDecompositionMapping[category][activity]
            for activity in self.categoryDecompositionMapping[category]:
                self.lines.append("              + " + activity + ": " + str(
                    self.categoryDecompositionMapping[category][activity]*100//categoryTime) + "%" + "\n")

    def produceTxtHourAnalysis(self):
        self.lines.append("Hourly Analysis" + "\n")

        print(self.hourDecompositionMapping)
        for hour in self.hourDecompositionMapping:
            categoryTime = 0
            self.lines.append("      - " + hour + ": " + "\n")
            for category in self.hourDecompositionMapping[hour]:
                categoryTime += self.hourDecompositionMapping[hour][category]
            for category in self.hourDecompositionMapping[hour]:
                self.lines.append("              + " + category + ": " + str(
                    self.hourDecompositionMapping[hour][category]*100//categoryTime) + "%" + "\n")

    def writeDocument(self):
        with open("[REPORT]" + self.date + ".txt", "w") as file:
            for line in self.lines:
                file.write(line)
