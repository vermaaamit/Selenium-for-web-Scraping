from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


from selenium import webdriver
driver = webdriver.Chrome()  # You can also use Firefox(), Edge(), etc.
driver.get("https://selenium-python.readthedocs.io/getting-started.html")
time.sleep(2)  # Wait for the page to load
driver.close()