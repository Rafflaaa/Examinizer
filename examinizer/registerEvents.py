import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from examinizer import utils


def registerToLecture(driver, module):
    driver.get(
        "https://hisinone.unibw.de/qisserver/pages/startFlow.xhtml?_flowId=studyPlanner-flow&_flowExecutionKey=e5s1")

    # Auf Alle Studientrimester und Termine setzen
    setTrimesterToAll(driver)

    # Sprung zu Modul
    path = utils.getHref(driver.execute_script("return document.body.innerHTML;"), module)
    driver.get(
        "https://hisinone.unibw.de" + str(path))

    clickElementById(driver, "detailViewData:tabContainer:term-planning-container:tabs:moduleChildrenTab")

    # Klick auf Vorlesung
    path = utils.getHrefLecture(driver.execute_script("return document.body.innerHTML;"), module)
    driver.get(
        "https://hisinone.unibw.de" + str(path))

    # Klick auf WT25
    clickElementById(driver,
                     "detailViewData:tabContainer:term-selection-container:termPeriodDropDownList")

    clickElementById(driver,
                     "detailViewData:tabContainer:term-selection-container:termPeriodDropDownList_0")

    # # Klick auf Anmelden
    # path = htmlParser.getHrefLecture(driver.execute_script("return document.body.innerHTML;"))
    # driver.get(
    #     "https://hisinone.unibw.de" + str(path))


def registerToExam(driver, module):
    driver.get(
        "https://hisinone.unibw.de/qisserver/pages/startFlow.xhtml?_flowId=studyPlanner-flow&_flowExecutionKey=e5s1")

    # Auf Alle Studientrimester und Termine setzen
    setTrimesterToAll(driver)

    # Sprung zu Modul
    path = utils.getHref(driver.execute_script("return document.body.innerHTML;"), module)
    driver.get(
        "https://hisinone.unibw.de" + str(path))

    # Click auf Veranstaltung
    clickElementById(driver, "detailViewData:tabContainer:term-planning-container:tabs:moduleChildrenTab")

    # Klick auf Pruefung
    path = utils.getHrefExam(driver.execute_script("return document.body.innerHTML;"), module)
    driver.get(
        "https://hisinone.unibw.de" + str(path))

    # Klick auf WT25
    clickElementById(driver,
                     "detailViewData:tabContainer:term-selection-container:termPeriodDropDownList")

    clickElementById(driver,
                     "detailViewData:tabContainer:term-selection-container:termPeriodDropDownList_0")

    # # Klick auf Anmelden
    # path = htmlParser.getHrefLecture(driver.execute_script("return document.body.innerHTML;"))
    # driver.get(
    #     "https://hisinone.unibw.de" + str(path))


def clickElementById(driver, idFromElement):
    clickable = driver.find_element(By.ID, idFromElement)
    ActionChains(driver) \
        .click(clickable) \
        .perform()


def setTrimesterToAll(driver):
    clickElementById(driver,
                     "enrollTree:activeView:selectedFsem")

    clickElementById(driver,
                     "enrollTree:activeView:selectedFsem_0")
    time.sleep(1)

    clickElementById(driver,
                     "enrollTree:activeView:selectedLectureTerm")

    clickElementById(driver,
                     "enrollTree:activeView:selectedLectureTerm_0")
    time.sleep(1)
