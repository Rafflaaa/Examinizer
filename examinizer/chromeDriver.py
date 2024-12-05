from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class ChromeDriver:

    def __init__(self):
        chrome_options = Options()
        # chrome_options.add_argument(r"--user-data-dir=C:\Users\nurba\ChromeProfiles")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    def startChrome(self):
        self.driver.get("https://hisinone.unibw.de/qisserver/pages/cs/sys/portal/hisinoneStartPage.faces")
