import datetime
from DayDataHandler import DayDataHandler
from ActivityMonitor import ActivityMonitor
from Analyzer import Analyzer
from time import time, sleep

dayDataHandler = DayDataHandler()
activityMonitor = ActivityMonitor()
dayStartKeyword = "Day Started"


def waitSomeSeconds(nbSeconds):
    sleep(nbSeconds - time() % nbSeconds)


def main():
    numberOfSecondsPerMeasurement = 60
    while True:
        yesterdayDate = (datetime.datetime.today() -
                         datetime.timedelta(days=1)).strftime("%m/%d/%Y")
        if yesterdayDate in dayDataHandler.getFirstTimeStamp():
            analyzer = Analyzer(dayDataHandler, yesterdayDate)
            analyzer.analyze(numberOfSecondsPerMeasurement)
            dayDataHandler.clear()
        else:
            process()
        waitSomeSeconds(numberOfSecondsPerMeasurement)


def process():
    currentActivity = activityMonitor.getActivity()
    dayDataHandler.record(currentActivity)


main()
