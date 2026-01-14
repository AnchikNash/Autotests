from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    TITLE = (By.CSS_SELECTOR, "h2")

    def check_title(self, expected_title):
        actual_title = self.get_text(self.TITLE)
        assert actual_title == expected_title


