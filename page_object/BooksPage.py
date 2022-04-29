from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BooksPage:
    first_book = 'div.a-section.octopus-pc-card-content li'

    def __init__(self, driver: webdriver):
        self.driver = driver

    def SelectFirstBookNouveautes(self):
        self.driver.find_elements(By.CSS_SELECTOR, self.first_book)[0].click()



