from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CartePage:
    liste_quantite_selector = "#quantity"




    def __init__(self, driver: webdriver):
        self.driver = driver

    def ChangeQantity(self, quantity):
        menu_deroulant = Select(self.driver.find_element(By.CSS_SELECTOR, self.liste_quantite_selector))
        menu_deroulant.select_by_visible_text(quantity)

    def GetQuantity(self):

        return Select(self.driver.find_element(By.CSS_SELECTOR, self.liste_quantite_selector)).first_selected_option.text












