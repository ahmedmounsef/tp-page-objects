from page_object.HomePage import HomePage
from page_object.BooksPage import BooksPage
from page_object.ProductPage import ProductPage
from page_object.ConfirmationPage import ConfirmationPage
from page_object.CartePage import CartePage

from selenium import webdriver
quantity = "2"

def test_amazon1():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.fr/")
    driver.maximize_window()
    driver.quit()

def test_page_object():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.fr/")
    driver.maximize_window()
    homePage = HomePage(driver)
    homePage.closeCookiePopup()
    homePage.openAllMenu()
    homePage.openBookCategory()
    homePage.openAllBooks()
    booksPage = BooksPage(driver)
    booksPage.SelectFirstBookNouveautes()
    productpage = ProductPage(driver)
    productpage.AddToCard()
    confirmationpage = ConfirmationPage(driver)
    confirmationpage.OpenCart()
    cartepage = CartePage(driver)
    cartepage.ChangeQantity("2")
    cartepage.GetQuantity()

    assert quantity == cartepage.GetQuantity()