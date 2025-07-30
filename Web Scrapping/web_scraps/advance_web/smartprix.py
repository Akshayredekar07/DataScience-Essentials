from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time 

# Setup Chrome options
options = Options()
options.add_argument('--start-maximized')

# Set ChromeDriver path
service = Service("C:/Users/Admin/Downloads/APPS/chromedriver.exe")

# Launch browser
driver = webdriver.Chrome(service=service, options=options)

# Open website
driver.get("https://us.smartprix.com/mobiles")
time.sleep(3)

# Apply filters - Assuming you want to click the first two options
driver.find_element(By.XPATH, '//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input').click()
time.sleep(2)

# Scroll logic
last_height = driver.execute_script('return document.body.scrollHeight')

scroll_count = 0
while True:
    scroll_count += 1
    print(f"Scrolling: {scroll_count}")
    # Scroll to bottom
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(2)

    new_height = driver.execute_script('return document.body.scrollHeight')

    if new_height == last_height:
        print("No more content to load.")
        break

    last_height = new_height

# Save HTML content to a file
html = driver.page_source

with open("smartprix.html", 'w', encoding="utf-8") as f:
    f.write(html)

print("HTML saved successfully.")

# Optional: Long wait for debugging
time.sleep(10)
driver.quit()
