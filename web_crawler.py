import time
from selenium import webdriver
from selenium.common.exceptions import WebDriverException


url = 'https://www.google.com/'


options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu') 
options.add_argument('--disable-dev-shm-usage')


# Define the maximum number of retries
max_retries = 10
retry_delay = 5 

# Initialize the WebDriver with retry
for retry in range(max_retries):
    try:
        driver = webdriver.Remote(
            command_executor='http://selenium-chrome:4444/wd/hub',
            options=options
        )
        break  # Successfully initialized WebDriver, exit retry loop
    except WebDriverException as e:
        print(f"Connection attempt {retry + 1} failed. Retrying in {retry_delay} seconds...")
        time.sleep(retry_delay)
else:
    raise Exception(f"Failed to connect to Selenium after {max_retries} attempts.")



driver.get(url)

print(driver.page_source)

driver.quit()
