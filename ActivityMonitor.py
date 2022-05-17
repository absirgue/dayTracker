from subprocess import Popen, PIPE


class ActivityMonitor:

    def __init__(self):
        pass

    def getWebsiteName(self):
        cmdNbSafariWindows = "osascript -e 'tell application \"Safari\" to return the number of windows'"
        pipeNbSafariWindow = Popen(
            cmdNbSafariWindows, shell=True, stdout=PIPE).stdout
        nbSafariWindow = pipeNbSafariWindow.readlines()[0]
        cmdActiveTab = "osascript -e 'tell app \"safari\" to get the url of the current tab of window " + nbSafariWindow + "'"
        pipeActiveTab = Popen(cmdActiveTab, shell=True, stdout=PIPE).stdout
        activeTabName = pipeActiveTab.readlines()
        try:
            cleanuper = activeTabName[0].split("/")[2].split(".")[:-1]
            websiteName = ''.join(cleanuper)
            return websiteName
        except Exception as e:
            return "Safari"

    def getActiveApp(self):
        mdNbSafariWindows = "osascript -e ' tell application \"System Events\" to get the name of first application process whose frontmost is true'"
        pipeActiveTab = Popen(
            mdNbSafariWindows, shell=True, stdout=PIPE).stdout
        activeTabName = pipeActiveTab.readlines()
        return activeTabName[0].strip()

    def getActivity(self):
        currentActivity = self.getActiveApp()
        if (currentActivity == "Safari"):
            currentActivity = self.getWebsiteName()
        return currentActivity
