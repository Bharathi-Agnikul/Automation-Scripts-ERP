import time
from ast import Index

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from urllib3 import request
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Payroll_Management:
    def __init__(self, driver):
        self.driver = driver

    def home_page(self):
        time.sleep(3)
        icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "(//i[@class='fa fa-credit-card-alt'])[2]"))
        )
        icon.click()
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element((By.CLASS_NAME, "preloader"))
        )
        homepage = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                                         "//span[text()='Home']")))
        homepage.click()
        time.sleep(2)
        # self.driver.save_screenshot('debug_screenshot.png')
        scrollable_element = self.driver.find_element(By.XPATH, "//main[@style='color: rgb(0, 0, 0);']")
        actions = ActionChains(self.driver)
        actions.move_to_element(scrollable_element).scroll_by_amount(0, 400).perform()
        # self.driver.execute_script("arguments[0].scrollTop += 500", scrollable_element)
        time.sleep(2)
        # action = ActionChains(self.driver)
        # action.scroll_by_amount(0, 500).perform()
        # view_all = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//span[@class='MuiTouchRipple-root css-w0pj6f'])[3]")))
        # view_all.click()

    def raise_request(self):
        menu = self.driver.find_element(By.XPATH, "//div[@class='menuicons MuiBox-root css-tj7rjq']")
        menu.click()
        time.sleep(2)
        #payslip
        payslip = self.driver.find_element(By.XPATH, "(//span[text()='Payslip'])[1]")
        payslip.click()
        time.sleep(2)
        from_date = self.driver.find_element(By.XPATH,
                                             "//div[@class='MuiInputBase-root MuiOutlinedInput-root MuiInputBase-colorPrimary MuiInputBase-formControl MuiInputBase-adornedEnd css-16ifayg']")
        self.driver.execute_script("arguments[0].value = 'January 2024';", from_date)
        # from_date = self.driver.find_element(By.XPATH, "//div[@class = 'MuiInputBase-root MuiOutlinedInput-root MuiInputBase-colorPrimary MuiInputBase-formControl MuiInputBase-adornedEnd css-16ifayg']")
        # from_date.send_keys("January 2024")
        time.sleep(2)
