import time
from datetime import datetime, timezone

from bs4 import BeautifulSoup


def getHrefLecture(html, module):
    soup = BeautifulSoup(html, 'html.parser')
    for a in soup.findAll("a", {"title": "Details für Veranstaltung '" + getModuleNameLecture(module) + "' anzeigen"}):
        return a["href"]


def getHrefExam(html, module):
    soup = BeautifulSoup(html, 'html.parser')
    getModuleNameExam(module)
    for a in soup.findAll("a", {"title": "Details für Prüfung '" + getModuleNameExam(module) + "' anzeigen"}):
        return a["href"]


def getHrefSubmit(html):
    soup = BeautifulSoup(html, 'html.parser')
    for button in soup.findAll("button", {"title": "Anmelden"}):
        return button["href"]


def getHref(html, module):
    soup = BeautifulSoup(html, 'html.parser')
    for a in soup.findAll(string=module, href=True):
        return a["href"]


def readFile(relativePathWithEnding):
    mylist = []
    file = open(relativePathWithEnding, mode="r", encoding="utf-8-sig")
    lines = file.readlines()
    file.close()
    for line in lines:
        mylist.append(line.strip())
    return mylist


def getModuleNameLecture(module):
    return module[7:]


def getModuleNameExam(module):
    module = cutTrailingNonRelevantSymbols(module)
    module = cutLeadingNonRelevantSymbols(module)
    return module


def cutTrailingNonRelevantSymbols(moduleName):
    if moduleName[-1:] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " "):
        return cutTrailingNonRelevantSymbols(moduleName[:-1])
    return moduleName


def cutLeadingNonRelevantSymbols(moduleName):
    if moduleName[0] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", "-"):
        return cutLeadingNonRelevantSymbols(moduleName[1:])
    return moduleName


def goodNight(endTimes, driver):
    endTimeArray = endTimes.split()
    currentTime = datetime.now(timezone.utc).astimezone()
    startTime = datetime(currentTime.year, currentTime.month, currentTime.day, currentTime.hour,
                         currentTime.minute).astimezone()
    end_time = datetime(int(endTimeArray[0]), int(endTimeArray[1]), int(endTimeArray[2]), int(endTimeArray[3]),
                        int(endTimeArray[4])).astimezone()

    x = False
    while not x:
        if startTime <= currentTime <= end_time:
            try:
                driver.refresh()
                time.sleep(60)
                currentTime = datetime.now(timezone.utc).astimezone()
            except:
                print('Current time is not between times')
        else:
            x = True
