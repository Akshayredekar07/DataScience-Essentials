from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Setup Chrome options
options = Options()
options.add_argument('--start-maximized')
# Uncomment if you want headless mode:
# options.add_argument('--headless')

# Provide path to your chromedriver
service = Service("C:/Users/Admin/Downloads/APPS/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

# Open AJIO search results
driver.get("https://www.ajio.com/search/?text=Backpack")
time.sleep(3)

# Scroll the page to load content dynamically
last_height = driver.execute_script("return document.body.scrollHeight")
scroll_counter = 1

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    new_height = driver.execute_script("return document.body.scrollHeight")
    print(f"Scroll #{scroll_counter}")
    scroll_counter += 1

    if new_height == last_height:
        break

    last_height = new_height

# Save entire HTML to file
html = driver.page_source

with open("ajio_backpack_full.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ HTML page saved as 'ajio_backpack_full.html'")

driver.quit()
