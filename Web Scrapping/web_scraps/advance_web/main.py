from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("CampusX")
search_box.send_keys(Keys.RETURN)

# Wait until search results load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "rso"))
)

# Find all search result links
links = driver.find_elements(By.XPATH, '//*[@id="rso"]//a')

# Click the second link (index 1, since it's 0-based)
if len(links) >= 2:
    driver.execute_script("arguments[0].click();", links[1])
else:
    print("Second link not found.")

# Keep the browser open
time.sleep(1000)
driver.quit()
