import os
from dotenv import load_dotenv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, StaleElementReferenceException

# load environment variables for  google form
path = os.path.join("Web scraping projects", "ZillowWebscrapeCapstone")
load_dotenv(os.path.join(path,".env"))
form_url = os.getenv("url")

"""
    DataLogger is a class of which each instantiation represents a single input into the google form.
    Has 1 function, which is input_data function, which takes 'data' as an argument. 
    'data' is made up of a single tuple (address, price, link) for a given listing. 
    Selenium webdriver is used to enter this information into google sheets. 
"""


class DataLogger():

    def __init__(self) -> None:
        # Initialize Selenium webdriver
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get(form_url)

    def input_data(self, data):

        time.sleep(5)

        # identify input fields
        input_fields = self.driver.find_elements(By.CSS_SELECTOR, 'input.whsOnd.zHQkBf')

        # address in first position
        input_fields[0].send_keys(data[0])

        # price in second position
        input_fields[1].send_keys(data[1])

        # link in third position
        input_fields[2].send_keys(data[2])

        submit_button = self.driver.find_element(By.CLASS_NAME, 'l4V7wb')
        submit_button.click()

        print(f'{data} submitted!')



