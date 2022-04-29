from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions
#from selenium.webdriver.support.wait import WebDriverWait


class ProductPage:

    ajouter_au_panier_selector = 'input[title="Ajouter au panier"]'


    def __init__(self, driver: webdriver):
        self.driver = driver


    def AddToCard(self):
        self.driver.find_element(By.CSS_SELECTOR, self.ajouter_au_panier_selector).click()






