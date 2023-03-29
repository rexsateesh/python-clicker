import os
import dotenv
import random
from time import sleep
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

dotenv.load_dotenv()

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless")
# chrome_options.headless = True # also works

hits = random.randint(20, 100)
print(f'Total number of hits: {hits}')

for i in range(hits):
    print(f'Opened browser: {i}')
    driver = webdriver.Chrome(options=chrome_options)
    start_url = os.environ.get('PAGE_URL')
    driver.get(start_url)

    sleep(random.randint(2, 4)) # Random sleep minutes

    elem = driver.find_element(By.XPATH, os.environ.get('ELEMENT_XPATH'))
    elem.click()

    sleep(1)
    print(f'Closed')
    
    # print(driver.page_source.encode("utf-8"))
    driver.quit()

