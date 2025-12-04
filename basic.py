from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Edge()
browser.get("https://www.qa-practice.com/elements/button/simple")

#click_buttom = browser.find_element(By.XPATH, "//input[@class='btn btn-primary']" )
#click_buttom.click()



click_buttom3 = browser.find_element(By.CSS_SELECTOR, 'input[class="btn btn-primary"]')
click_buttom3.click()
sleep(1)