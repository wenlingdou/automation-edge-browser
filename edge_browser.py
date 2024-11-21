import datetime 
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configure Edge options
options = Options()
options.add_argument("--start-maximized")  # Optional: Start browser maximized

# Set up the Edge WebDriver
service = Service("C:/Users/1984w/Downloads/edgedriver_win64/msedgedriver.exe")  # Replace with the path to your EdgeDriver executable
driver = webdriver.Edge(service=service, options=options)

try:
    # Open Google
    driver.get("https://www.google.com")
    print("-----------Google webpage opened-----------------")

    # Locate the search box, enter the query, and submit
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys("Novarc Technologies")
    search_box.submit()
    print("---------Trying to search for Novarc Technologies----------------")

    # Wait for search results to load and display the link
    results = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "search"))
    )

    # Find the first result link
    first_result = results.find_element(By.XPATH, "//h3[contains(text(), 'Novarc Technologies')]/ancestor::a")
    first_result.click()
    print("---------------Welcome to Novarc Technologies------------------")

    # Wait for 30 seconds on the company's website
    time.sleep(30)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Quit the browser
    driver.quit()

print(f'---------The test is completed on {datetime.datetime.now()}.-------------')

