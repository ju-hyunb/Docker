from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service



options = Options()
options.add_argument("--headless")
options.add_argument("no-sandbox")
options.add_argument("--disable-extensions")
options.add_argument('--disable-dev-shm-usage')
driver =webdriver.Chrome(service=Service('/usr/bin/chromedriver'), options=options)


url = input("Press URL :")
driver.get(url)
print("page title : ", driver.title)
