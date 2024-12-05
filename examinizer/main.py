import time

from examinizer import utils, registerEvents
from examinizer.chromeDriver import ChromeDriver

chromeDriver = ChromeDriver()
chromeDriver.startChrome()

time.sleep(20)
modules = utils.readFile("../config/modules.txt")
utils.goodNight(modules[0], chromeDriver.driver)
modules = modules[1:]

for module in modules:
    registerEvents.registerToLecture(chromeDriver.driver, module)
    time.sleep(1)
    registerEvents.registerToExam(chromeDriver.driver, module)
    time.sleep(1)

chromeDriver.driver.quit()
