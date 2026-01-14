from itertools import count

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    GALAXY_S6 = (By.XPATH, "//a[text()='Samsung galaxy s6']")

    def open_home(self):
        self.open("https://demoblaze.com/")

    def click_galaxy_s6(self):
        self.click(self.GALAXY_S6)
