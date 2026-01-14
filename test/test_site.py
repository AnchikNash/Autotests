from pages.homepage import HomePage
from pages.product_page import ProductPage

def test_open_samsung(browser):
    home = HomePage(browser)
    product = ProductPage(browser)

    home.open_home()
    home.click_galaxy_s6()
    product.check_title("Samsung galaxy s6")


