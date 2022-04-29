from selenium import webdriver
from selenium.webdriver.common.by import By


class ConfirmationPage:
    aller_au_panier_selector = 'a[href="/gp/cart/view.html?ref_=sw_gtc"]'

    def __init__(self, driver: webdriver):
        self.driver = driver

    def OpenCart(self):
        self.driver.find_element(By.CSS_SELECTOR, self.aller_au_panier_selector).click()




