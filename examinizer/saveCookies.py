import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument(r"--user-data-dir=C:\Users\nurba\ChromeProfiles")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
chrome_options.add_argument(r"user-data-dir=C:\Users\nurba\ChromeProfiles")
driver.get("https://hisinone.unibw.de/qisserver/pages/cs/sys/portal/hisinoneStartPage.faces")
time.sleep(30)  # Time to enter credentials
driver.quit()
