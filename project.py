from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
query = "speaker"
file =0
for i in range(1, 3):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=X79A61GQ1NB6&sprefix=speaker%2Caps%2C232&ref=nb_sb_noss_2")
    elem = driver.find_elements(By.CLASS_NAME, "puisg-col")
    print(f"{len(elem)} elements found on page {i}")
    for e in elem:
        d = e.get_attribute("outerHTML")
        with open(f"data/{query}_{file}.html", "w", encoding="utf-8") as f:
            f.write(d)
            file += 1
    time.sleep(2)  # Wait for the page to load
driver.quit()


